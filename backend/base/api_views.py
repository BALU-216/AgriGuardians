import json
import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm
from .models import PredictionHistory
from .utils import predict_disease


def _error(message, status=400, details=None):
    data = {"error": message}
    if details:
        data["details"] = details
    return JsonResponse(data, status=status)


@csrf_exempt
def api_signup(request):
    if request.method != "POST":
        return _error("POST required", 405)
    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return _error("Invalid JSON")

    form = SignUpForm(data=data)
    if not form.is_valid():
        details = {k: [str(e) for e in v] for k, v in form.errors.items()}
        return _error("Please correct the form errors.", 400, details)
    form.save()
    return JsonResponse({"message": "Signup successful"}, status=201)


@csrf_exempt
def api_login(request):
    if request.method != "POST":
        return _error("POST required", 405)
    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return _error("Invalid JSON")

    user = authenticate(request, email=data.get("email", ""), password=data.get("password", ""))
    if user is None:
        return _error("Invalid email or password", 401)
    login(request, user)
    return JsonResponse({"message": "Login successful", "user": {"id": user.id, "email": user.email}})

@csrf_exempt
@login_required
def api_me(request):
    return JsonResponse({"authenticated": True, "user": {"id": request.user.id, "email": request.user.email, "first_name": request.user.first_name, "last_name": request.user.last_name}})


@login_required
def api_predict(request):
    if request.method != "POST":
        return _error("POST required", 405)
    img = request.FILES.get("image")
    if not img:
        return _error("Please upload a leaf image.")

    saved_name = default_storage.save(f"prediction_images/{img.name}", img)
    file_path = default_storage.path(saved_name)
    results = predict_disease(file_path)
    if not results:
        return _error("No prediction was produced.", 500)

    top = results[0]
    history = PredictionHistory.objects.create(
        user=request.user,
        image=saved_name,
        crop=top["crop"],
        disease=top["disease"],
        confidence=top["confidence"],
    )
    return JsonResponse({"results": results, "history_id": history.id, "image_url": default_storage.url(saved_name)})


@login_required
def api_history(request):
    rows = PredictionHistory.objects.filter(user=request.user).order_by("-created_at")
    history = []
    for row in rows:
        history.append({
            "id": row.id,
            "crop": row.crop,
            "disease": row.disease,
            "confidence": row.confidence,
            "created_at": row.created_at.isoformat(),
            "image_url": row.image.url if row.image else "",
        })
    return JsonResponse({"history": history})
