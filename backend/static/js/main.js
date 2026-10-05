/* ─── Leaf Network Canvas ─────────────────────────────── */

const canvas = document.getElementById("networkCanvas");
const ctx    = canvas.getContext("2d");

// 🌿 Load leaf image (from index.html variable)
const leafImg = new Image();
leafImg.src = window.leafImagePath;

function resizeCanvas() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
}

resizeCanvas();
window.addEventListener("resize", resizeCanvas);

const nodeCount = 30;

const nodes = Array.from({ length: nodeCount }, () => ({
    x:  Math.random() * canvas.width,
    y:  Math.random() * canvas.height,
    vx: (Math.random() - 0.5) * 0.4,
    vy: (Math.random() - 0.5) * 0.4,
}));

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i];

        // Move
        n.x += n.vx;
        n.y += n.vy;

        // Bounce
        if (n.x < 0 || n.x > canvas.width)  n.vx *= -1;
        if (n.y < 0 || n.y > canvas.height) n.vy *= -1;

        // 🌿 Draw leaf
        ctx.globalAlpha = 0.35;
        ctx.drawImage(leafImg, n.x - 10, n.y - 10, 20, 20);
        ctx.globalAlpha = 1;

        // 🔗 Connections
        for (let j = i + 1; j < nodes.length; j++) {
            const o  = nodes[j];
            const dx = n.x - o.x;
            const dy = n.y - o.y;
            const d  = Math.sqrt(dx * dx + dy * dy);

            if (d < 130) {
                ctx.beginPath();
                ctx.moveTo(n.x, n.y);
                ctx.lineTo(o.x, o.y);

                ctx.strokeStyle =
                    `rgba(120,160,120,${0.15 * (1 - d / 130)})`;

                ctx.lineWidth = 0.7;
                ctx.stroke();
            }
        }
    }

    requestAnimationFrame(draw);
}

// ▶️ Start animation AFTER image loads
leafImg.onload = () => draw();

/* ─── Navbar Shrink on Scroll ───────────────────────────── */
const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
    navbar.classList.toggle("shrink", window.scrollY > 60);
});


/* ─── Mobile Menu Toggle ────────────────────────────────── */
const hamburger  = document.getElementById("hamburger");
const mobileMenu = document.getElementById("mobileMenu");

if (hamburger && mobileMenu) {
    hamburger.addEventListener("click", () => {
        mobileMenu.classList.toggle("open");
    });

    // Close when a link is tapped
    mobileMenu.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => mobileMenu.classList.remove("open"));
    });
}


/* ─── Scroll-triggered card reveal ─────────────────────── */
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll(".feature-card, .step-card").forEach(el => {
    el.style.opacity    = "0";
    el.style.transform  = "translateY(24px)";
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(el);
});


// ── Toast Auto-dismiss ──────────────────────────────────
setTimeout(() => {
    document.querySelectorAll(".toast").forEach(t => {
        t.style.animation = "slideOut 0.4s ease forwards";
        setTimeout(() => t.remove(), 400);
    });
}, 4000);