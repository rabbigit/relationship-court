"""The Supreme Court of Our Relationship — a playful Streamlit quiz."""

from html import escape

import streamlit as st
import streamlit.components.v1 as components


# -----------------------------------------------------------------------------
# PERSONALIZE THESE TWO LINES
# -----------------------------------------------------------------------------
PARTNER_NAME = "My Love"
YOUR_NAME = "Rabbi"


st.set_page_config(
    page_title="The Supreme Court of Our Relationship",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 12% 15%, rgba(255,255,255,.72), transparent 25%),
                radial-gradient(circle at 88% 8%, rgba(255,222,232,.85), transparent 24%),
                linear-gradient(145deg, #fff8fa 0%, #ffe8ee 46%, #fbd4df 100%);
        }
        header[data-testid="stHeader"], footer { display: none; }
        .block-container { max-width: 980px; padding: 1rem 0.75rem 2rem; }
        iframe { border-radius: 26px; }
    </style>
    """,
    unsafe_allow_html=True,
)


HTML_TEMPLATE = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Supreme Court of Our Relationship</title>
<style>
    :root {
        --wine: #7f1734;
        --rose: #c93964;
        --pink: #f47ca0;
        --pale: #fff1f5;
        --cream: #fffaf8;
        --ink: #351421;
        --muted: #735461;
        --gold: #d6a546;
        --shadow: 0 24px 70px rgba(111, 19, 50, .18);
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
        margin: 0;
        min-height: 100vh;
        overflow-x: hidden;
        color: var(--ink);
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
                     "Segoe UI", sans-serif;
        background:
            radial-gradient(circle at 10% 10%, rgba(255,255,255,.95), transparent 24%),
            radial-gradient(circle at 90% 12%, rgba(255,216,229,.9), transparent 25%),
            linear-gradient(145deg, #fff9fb 0%, #ffe7ef 52%, #fbd4e0 100%);
    }

    button { font: inherit; }

    .app-shell {
        position: relative;
        width: min(920px, calc(100% - 24px));
        min-height: 850px;
        margin: 12px auto;
        padding: 34px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,.92);
        border-radius: 30px;
        background: rgba(255, 250, 250, .88);
        box-shadow: var(--shadow);
        backdrop-filter: blur(12px);
    }

    .app-shell::before,
    .app-shell::after {
        content: "";
        position: absolute;
        z-index: 0;
        width: 270px;
        height: 270px;
        border-radius: 50%;
        filter: blur(4px);
        opacity: .42;
        pointer-events: none;
    }

    .app-shell::before {
        top: -150px;
        right: -90px;
        background: #ffd1df;
    }

    .app-shell::after {
        bottom: -160px;
        left: -100px;
        background: #f7b7ca;
    }

    .screen { position: relative; z-index: 2; }
    .hidden { display: none !important; }

    .eyebrow {
        margin: 0 0 16px;
        color: var(--rose);
        font-size: .78rem;
        font-weight: 850;
        letter-spacing: .15em;
        text-transform: uppercase;
    }

    h1, h2, h3, p { margin-top: 0; }

    h1 {
        max-width: 760px;
        margin-bottom: 18px;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.35rem, 7vw, 5.1rem);
        line-height: .98;
        letter-spacing: -.045em;
        color: var(--wine);
    }

    h2 {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.8rem, 4.8vw, 3.25rem);
        line-height: 1.08;
        color: var(--wine);
    }

    .lede {
        max-width: 680px;
        color: var(--muted);
        font-size: clamp(1rem, 2.2vw, 1.2rem);
        line-height: 1.72;
    }

    .personal-note {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        margin: 8px 0 28px;
        padding: 10px 15px;
        color: var(--wine);
        border: 1px solid #f3b9ca;
        border-radius: 999px;
        background: #fff5f8;
        font-weight: 750;
    }

    .seal {
        display: grid;
        place-items: center;
        width: 104px;
        height: 104px;
        margin-bottom: 26px;
        border: 2px solid #edb4c5;
        border-radius: 50%;
        background: linear-gradient(145deg, #fff, #ffe6ee);
        box-shadow: 0 14px 35px rgba(127, 23, 52, .14);
        font-size: 3rem;
        animation: breathe 2.4s ease-in-out infinite;
    }

    .notice {
        max-width: 690px;
        margin: 25px 0;
        padding: 15px 18px;
        color: #6a3345;
        border-left: 4px solid var(--pink);
        border-radius: 0 14px 14px 0;
        background: #fff2f6;
        line-height: 1.55;
    }

    .primary,
    .secondary {
        min-height: 52px;
        padding: 13px 24px;
        border-radius: 999px;
        cursor: pointer;
        font-weight: 850;
        transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
    }

    .primary {
        color: white;
        border: 0;
        background: linear-gradient(135deg, var(--wine), var(--rose));
        box-shadow: 0 13px 28px rgba(127, 23, 52, .25);
    }

    .secondary {
        color: var(--wine);
        border: 1px solid #eeb2c4;
        background: #fff8fa;
    }

    .primary:hover,
    .secondary:hover { transform: translateY(-2px); }
    .primary:active,
    .secondary:active { transform: translateY(0); }
    .primary:focus-visible,
    .secondary:focus-visible,
    .answer-option:focus-visible {
        outline: 4px solid rgba(201, 57, 100, .25);
        outline-offset: 3px;
    }

    #start-screen {
        min-height: 760px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        padding: clamp(10px, 4vw, 48px);
    }

    #quiz-screen { padding: clamp(4px, 3vw, 24px); }

    .quiz-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 12px;
    }

    .counter {
        color: var(--rose);
        font-size: .85rem;
        font-weight: 850;
        letter-spacing: .08em;
        text-transform: uppercase;
    }

    .progress-track {
        height: 9px;
        margin: 15px 0 42px;
        overflow: hidden;
        border-radius: 999px;
        background: #f6dce4;
    }

    .progress-fill {
        width: 0;
        height: 100%;
        border-radius: inherit;
        background: linear-gradient(90deg, var(--pink), var(--wine));
        transition: width .45s ease;
    }

    .question-card {
        min-height: 570px;
        padding: clamp(24px, 5vw, 50px);
        border: 1px solid #f4cad6;
        border-radius: 25px;
        background: linear-gradient(160deg, rgba(255,255,255,.96), rgba(255,243,247,.9));
        box-shadow: 0 18px 45px rgba(113, 28, 55, .1);
    }

    .question-number {
        color: var(--gold);
        font-size: .8rem;
        font-weight: 900;
        letter-spacing: .14em;
        text-transform: uppercase;
    }

    .question-text {
        min-height: 145px;
        margin: 14px 0 34px;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.55rem, 4.3vw, 2.7rem);
        line-height: 1.18;
        color: var(--ink);
    }

    .answer-zone {
        position: relative;
        display: grid;
        grid-template-columns: 1fr 1fr;
        align-items: center;
        gap: 18px;
        min-height: 112px;
        padding: 12px 0;
    }

    .answer-option {
        position: relative;
        z-index: 3;
        width: 100%;
        min-height: 72px;
        padding: 14px 18px;
        color: var(--ink);
        border: 2px solid #efbdcc;
        border-radius: 18px;
        background: #fff;
        box-shadow: 0 8px 20px rgba(91, 27, 48, .08);
        cursor: pointer;
        font-weight: 780;
        line-height: 1.35;
        transition: transform .15s ease, border-color .18s ease,
                    background .18s ease, color .18s ease;
        touch-action: manipulation;
    }

    .answer-option.forced:hover {
        border-color: var(--rose);
        background: #fff4f7;
    }

    .answer-option.selected {
        color: #fff;
        border-color: var(--wine);
        background: linear-gradient(135deg, var(--wine), var(--rose));
        box-shadow: 0 14px 30px rgba(127, 23, 52, .23);
    }

    .answer-option.escape {
        border-style: dashed;
        color: #7a5964;
    }

    .question-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 18px;
        margin-top: 28px;
    }

    .choice-status {
        min-height: 24px;
        color: var(--rose);
        font-size: .92rem;
        font-weight: 760;
    }

    #next-btn { opacity: 0; pointer-events: none; }
    #next-btn.ready { opacity: 1; pointer-events: auto; animation: pop .35s ease; }

    .toast {
        position: fixed;
        z-index: 50;
        left: 50%;
        bottom: 28px;
        width: min(440px, calc(100% - 32px));
        padding: 14px 20px;
        color: white;
        border-radius: 999px;
        background: rgba(87, 16, 40, .96);
        box-shadow: 0 15px 40px rgba(63, 10, 28, .3);
        text-align: center;
        font-weight: 800;
        opacity: 0;
        transform: translate(-50%, 20px);
        pointer-events: none;
        transition: opacity .2s ease, transform .2s ease;
    }

    .toast.show { opacity: 1; transform: translate(-50%, 0); }

    #review-screen {
        min-height: 760px;
        padding: clamp(20px, 5vw, 54px);
    }

    .review-panel {
        padding: clamp(22px, 4vw, 38px);
        border: 1px solid #efc2cf;
        border-radius: 24px;
        background: #fff;
        box-shadow: 0 18px 45px rgba(111, 19, 50, .11);
    }

    .scan-line {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 13px 0;
        color: var(--muted);
        animation: fadeUp .35s ease both;
    }

    .scan-line::before {
        content: "✓";
        display: grid;
        place-items: center;
        flex: 0 0 25px;
        width: 25px;
        height: 25px;
        color: #fff;
        border-radius: 50%;
        background: var(--rose);
        font-size: .78rem;
        font-weight: 900;
    }

    .findings {
        margin-top: 24px;
        padding: 20px;
        border-radius: 18px;
        background: #fff3f6;
        animation: fadeUp .45s ease both;
    }

    .finding-row {
        display: flex;
        justify-content: space-between;
        gap: 22px;
        padding: 9px 0;
        border-bottom: 1px solid #f3d5de;
    }

    .finding-row:last-child { border-bottom: 0; }
    .finding-row strong { color: var(--wine); text-align: right; }

    .system-error {
        margin-top: 25px;
        padding: 22px;
        color: #791a35;
        border: 2px solid #d84c73;
        border-radius: 18px;
        background: #fff0f4;
        box-shadow: 0 0 0 7px rgba(216, 76, 115, .08);
        animation: alarm .65s ease-in-out infinite alternate;
    }

    .system-error h3 { margin-bottom: 8px; font-size: 1.35rem; }

    #verdict-btn,
    #sentence-btn { margin-top: 24px; }

    #verdict-screen {
        padding: clamp(10px, 4vw, 38px);
        text-align: center;
    }

    .verdict-stamp {
        display: inline-block;
        margin: 4px 0 20px;
        padding: 9px 16px;
        color: var(--wine);
        border: 2px solid var(--wine);
        border-radius: 10px;
        font-weight: 950;
        letter-spacing: .13em;
        text-transform: uppercase;
        transform: rotate(-3deg);
        animation: stamp .55s cubic-bezier(.18,.89,.32,1.28) both;
    }

    .verdict-card {
        padding: clamp(24px, 5vw, 52px);
        border: 1px solid #f0c4d0;
        border-radius: 26px;
        background: linear-gradient(150deg, #fff, #fff3f7);
        box-shadow: 0 20px 55px rgba(111, 19, 50, .14);
    }

    .verdict-title {
        margin-bottom: 22px;
        font-size: clamp(2rem, 6vw, 4.25rem);
    }

    .love-line {
        margin: 25px 0;
        color: var(--rose);
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(1.8rem, 5vw, 3.2rem);
        font-weight: 800;
    }

    .verdict-copy {
        max-width: 700px;
        margin: 0 auto;
        color: #60404c;
        font-size: 1.04rem;
        line-height: 1.75;
    }

    .verdict-copy p { margin-bottom: 16px; }

    .sentence {
        max-width: 660px;
        margin: 34px auto;
        padding: 25px;
        border: 1px solid #edbdca;
        border-radius: 22px;
        background: #fff7f9;
        text-align: left;
    }

    .sentence h3 {
        color: var(--wine);
        font-family: Georgia, "Times New Roman", serif;
        font-size: 1.6rem;
    }

    .sentence ul {
        margin: 0;
        padding-left: 22px;
        color: #664653;
        line-height: 1.85;
    }

    #court-sentence-section {
        animation: fadeUp .55s ease both;
    }

    .case-closed {
        margin: 25px 0 10px;
        color: var(--wine);
        font-size: clamp(1.6rem, 4vw, 2.5rem);
        font-weight: 950;
        letter-spacing: .04em;
    }

    .signature {
        color: var(--muted);
        font-family: Georgia, "Times New Roman", serif;
        font-style: italic;
    }

    .floating-heart,
    .confetti {
        position: fixed;
        z-index: 1;
        top: -10vh;
        pointer-events: none;
        user-select: none;
        animation: fall linear forwards;
    }

    .floating-heart { color: rgba(201,57,100,.18); }
    .confetti { z-index: 100; }

    @keyframes breathe {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.06); }
    }

    @keyframes pop {
        from { transform: scale(.88); }
        to { transform: scale(1); }
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes alarm {
        from { transform: translateX(-2px); }
        to { transform: translateX(2px); }
    }

    @keyframes stamp {
        from { opacity: 0; transform: scale(2.2) rotate(-8deg); }
        to { opacity: 1; transform: scale(1) rotate(-3deg); }
    }

    @keyframes fall {
        to { transform: translateY(120vh) rotate(720deg); opacity: .15; }
    }

    @media (max-width: 680px) {
        .app-shell { width: calc(100% - 10px); margin: 5px auto; padding: 15px; border-radius: 22px; }
        #start-screen { min-height: 760px; padding: 18px; }
        .seal { width: 84px; height: 84px; font-size: 2.4rem; }
        .question-card { min-height: 640px; padding: 24px 18px; }
        .question-text { min-height: 190px; }
        .answer-zone { grid-template-columns: 1fr; min-height: 190px; }
        .question-footer { align-items: stretch; flex-direction: column; }
        #next-btn { width: 100%; }
        .finding-row { flex-direction: column; gap: 3px; }
        .finding-row strong { text-align: left; }
        #verdict-screen { padding: 4px; }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            scroll-behavior: auto !important;
            animation-duration: .01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: .01ms !important;
        }
    }
</style>
</head>
<body>
<main class="app-shell">
    <section id="start-screen" class="screen">
        <div class="seal" aria-hidden="true">⚖️</div>
        <p class="eyebrow">Official relationship proceedings</p>
        <h1>The Supreme Court of Our Relationship</h1>
        <p class="lede">
            A completely serious, perfectly fair, and absolutely not-rigged
            investigation into your recent request to go away from my life.
        </p>
        <div class="personal-note">❤️ For __PARTNER_NAME__, from __YOUR_NAME__</div>
        <div class="notice">
            Please answer honestly. Loving answers may behave suspiciously,
            disappear unexpectedly, or run away from your cursor.
        </div>
        <button id="start-btn" class="primary" type="button">Enter the Courtroom</button>
    </section>

    <section id="quiz-screen" class="screen hidden" aria-live="polite">
        <div class="quiz-top">
            <p class="eyebrow" style="margin:0">Relationship examination</p>
            <span id="counter" class="counter">Question 1 of 14</span>
        </div>
        <div class="progress-track" aria-hidden="true">
            <div id="progress-fill" class="progress-fill"></div>
        </div>

        <article class="question-card">
            <div id="question-number" class="question-number">Question 1</div>
            <div id="question-text" class="question-text"></div>
            <div id="answer-zone" class="answer-zone"></div>
            <div class="question-footer">
                <div id="choice-status" class="choice-status">Choose your answer carefully.</div>
                <button id="next-btn" class="primary" type="button">Next Question</button>
            </div>
        </article>
    </section>

    <section id="review-screen" class="screen hidden">
        <p class="eyebrow">Emergency relationship review</p>
        <h2>🚨 The Court is analyzing your answers</h2>
        <div class="review-panel">
            <div id="scan-lines" aria-live="polite"></div>

            <div id="findings" class="findings hidden">
                <h3>Preliminary findings</h3>
                <div class="finding-row"><span>Love detected</span><strong>0%</strong></div>
                <div class="finding-row"><span>Missing me</span><strong>Absolutely not</strong></div>
                <div class="finding-row"><span>Growing old together</span><strong>Rejected</strong></div>
                <div class="finding-row"><span>Emotional support</span><strong>Permanently closed</strong></div>
                <div class="finding-row"><span>Applicant's villain status</span><strong>Confirmed</strong></div>
                <div class="finding-row"><span>Desire to remove me</span><strong>Extremely high</strong></div>
            </div>

            <div id="system-error" class="system-error hidden">
                <h3>⚠️ SYSTEM ERROR</h3>
                <p>The Court attempted to approve your application.</p>
                <p><strong>However, my heart refused to process the request.</strong></p>
                <p>Recalculating... Reconsidering... Overruling the examination...</p>
            </div>
        </div>
        <button id="verdict-btn" class="primary hidden" type="button">See the Final Verdict ❤️</button>
    </section>

    <section id="verdict-screen" class="screen hidden">
        <div class="verdict-card">
            <div class="verdict-stamp">Final verdict</div>
            <h2 class="verdict-title">Your application to leave my life has been rejected ❤️</h2>

            <div class="verdict-copy">
                <p>Even if you claim that you hate me...</p>
                <p>Even if you insist that you never miss me...</p>
                <p>Even if you choose peace over my nonsense...</p>

                <div class="love-line">I will still choose you ❤️</div>

                <p>
                    I will not let distance, misunderstandings, difficult days, or
                    moments of doubt take away what we have without fighting for us.
                </p>
                <p>
                    You are the person I chose with all my heart—and the person
                    I would continue to choosing.
                </p>
                <p>
                    When life becomes difficult, I want us to stay, talk, understand,
                    forgive, and find our way back to each other.
                </p>
                <p>
                    So, no—I do not want to let you disappear from my life. Not today.
                    Not because of distance. Not because of difficult moments.
                </p>
                <p>
                    And certainly not after you have accumulated such an enormous
                    unpaid balance of hugs and kisses.
                </p>
            </div>

            <button id="sentence-btn" class="primary" type="button">See Our Court Sentence ⚖️</button>

            <div id="court-sentence-section" class="hidden">
                <div class="sentence">
                    <h3>OUR SENTENCE</h3>
                    <p>You are hereby sentenced to:</p>
                    <ul>
                        <li>One lifetime of annoying messages</li>
                        <li>Unlimited random phone calls</li>
                        <li>Teasing</li>
                        <li>Every future moment celebrated together</li>
                        <li>Peaceful naps with my head in your lap</li>
                        <li>Growing old and wrinkly beside me</li>
                        <li>Repayment of every missed hug</li>
                        <li>All overdue kisses—with compound interest</li>
                    </ul>
                </div>

                <div class="case-closed">CASE CLOSED 🔨❤️</div>
                <p>Appeals require one extremely long hug and no fewer than million kisses. 😘</p>
                <p class="signature">Forever yours, __YOUR_NAME__</p>
                <button id="restart-btn" class="secondary" type="button">Review the case again</button>
            </div>
        </div>
    </section>
</main>

<div id="toast" class="toast" role="status" aria-live="polite"></div>

<script>
const questions = [
    {
        text: "Do you really, truly, and genuinely hate me?",
        options: ["Yes, completely.", "No, never."],
        forced: 0
    },
    {
        text: "Can you really go an entire day without missing me?",
        options: ["Yes, easily.", "No, not at all."],
        forced: 0
    },
    {
        text: "Do you believe distance is stronger than my stubborn love for you?",
        options: ["Yes, it is.", "No, never."],
        forced: 0
    },
    {
        text: "Do you believe that your heart genuinely loves me? 😛",
        options: ["Yes, I do.", "No, I do not."],
        forced: 1
    },
    {
        text: "Would your life genuinely be better without my annoying messages, random calls, and teasing?",
        options: ["Yes, much better.", "No, definitely not."],
        forced: 0
    },
    {
        text: "When this distance finally ends, do you want to hold me tightly until we recover every hug we have missed?",
        options: ["Yes, absolutely.", "No, not really."],
        forced: 1
    },
    {
        text: "When life becomes difficult, do you want us to fight for our relationship instead of disappearing?",
        options: ["Yes, always.", "No, I do not."],
        forced: 1
    },
    {
        text: "Would you remove me from your life in exchange for a peaceful, completely drama-free existence?",
        options: ["Yes, immediately.", "No, never."],
        forced: 0
    },
    {
        text: "Do you want me to be your safe place?",
        options: ["Yes, always.", "No, I do not."],
        forced: 1
    },
    {
        text: "Do you want to be the person I can come to whenever life feels too heavy?",
        options: ["Yes, always.", "No, I do not."],
        forced: 1
    },
    {
        text: "Do you want me beside you through every moment of life?",
        options: ["Yes, every moment.", "No, not really."],
        forced: 1
    },
    {
        text: "Do you want us to grow old together—even when we are wrinkly and still arguing about who loves whom more?",
        options: ["Yes, absolutely.", "No, I do not."],
        forced: 1
    },
    {
        text: "When you see me hurting or struggling, do you enjoy watching me suffer?",
        options: ["Yes, I do.", "No, never."],
        forced: 0
    },
    {
        text: "When I am unable to sleep, would you let me rest peacefully with my head in your lap and your arms around me?",
        options: ["Yes, always.", "No, I would not."],
        forced: 1
    }
];

const rejectionMessages = [
    "That answer appears to be too loving for this investigation.",
    "Objection! The Court will not allow such tenderness.",
    "Nice try. That answer has escaped.",
    "The cursor has been instructed not to cooperate.",
    "Suspicious affection detected. Please try the other answer.",
    "This Court accepts only dramatically terrible answers today."
];

const scanMessages = [
    "Analyzing all fourteen answers...",
    "Examining shared memories...",
    "Calculating accumulated hug debt...",
    "Measuring distance against stubborn love...",
    "Confirming alleged hatred...",
    "Consulting the Department of Love and Long-Distance Affairs..."
];

let currentQuestion = 0;
let questionAnswered = false;
let toastTimer = null;
let reviewTimers = [];

const startScreen = document.getElementById("start-screen");
const quizScreen = document.getElementById("quiz-screen");
const reviewScreen = document.getElementById("review-screen");
const verdictScreen = document.getElementById("verdict-screen");
const questionText = document.getElementById("question-text");
const questionNumber = document.getElementById("question-number");
const answerZone = document.getElementById("answer-zone");
const counter = document.getElementById("counter");
const progressFill = document.getElementById("progress-fill");
const choiceStatus = document.getElementById("choice-status");
const nextBtn = document.getElementById("next-btn");
const toast = document.getElementById("toast");
const verdictBtn = document.getElementById("verdict-btn");
const sentenceBtn = document.getElementById("sentence-btn");
const courtSentenceSection = document.getElementById("court-sentence-section");

function showScreen(screen) {
    [startScreen, quizScreen, reviewScreen, verdictScreen].forEach(item => item.classList.add("hidden"));
    screen.classList.remove("hidden");
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function startQuiz() {
    currentQuestion = 0;
    questionAnswered = false;
    verdictBtn.classList.add("hidden");
    sentenceBtn.classList.remove("hidden");
    courtSentenceSection.classList.add("hidden");
    showScreen(quizScreen);
    renderQuestion();
}

function renderQuestion() {
    const question = questions[currentQuestion];
    questionAnswered = false;
    questionNumber.textContent = `Question ${currentQuestion + 1}`;
    counter.textContent = `Question ${currentQuestion + 1} of ${questions.length}`;
    questionText.textContent = question.text;
    progressFill.style.width = `${(currentQuestion / questions.length) * 100}%`;
    choiceStatus.textContent = "Choose your answer carefully.";
    nextBtn.classList.remove("ready");
    nextBtn.textContent = currentQuestion === questions.length - 1
        ? "Submit My Answers ❤️"
        : "Next Question";

    answerZone.innerHTML = "";
    question.options.forEach((label, index) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = `answer-option ${index === question.forced ? "forced" : "escape"}`;
        button.textContent = label;
        button.setAttribute("aria-label", label);

        if (index === question.forced) {
            button.addEventListener("click", () => selectForcedAnswer(button));
        } else {
            button.addEventListener("pointerenter", () => evade(button));
            button.addEventListener("focus", () => evade(button));
            button.addEventListener("click", event => rejectLovingAnswer(event, button));
        }
        answerZone.appendChild(button);
    });
}

function selectForcedAnswer(button) {
    if (questionAnswered) return;
    questionAnswered = true;
    document.querySelectorAll(".answer-option").forEach(item => {
        item.classList.remove("selected");
        item.setAttribute("aria-pressed", "false");
    });
    button.classList.add("selected");
    button.setAttribute("aria-pressed", "true");
    choiceStatus.textContent = "Answer recorded by the Court. ⚖️";
    progressFill.style.width = `${((currentQuestion + 1) / questions.length) * 100}%`;
    nextBtn.classList.add("ready");
}

function evade(button) {
    if (questionAnswered) return;
    const mobile = window.innerWidth < 680;
    const maxX = mobile ? 30 : 74;
    const maxY = mobile ? 7 : 13;
    let x = Math.round((Math.random() * 2 - 1) * maxX);
    let y = Math.round((Math.random() * 2 - 1) * maxY);
    if (Math.abs(x) < 18) x = x < 0 ? -30 : 30;
    button.style.transform = `translate(${x}px, ${y}px) rotate(${(Math.random() * 4 - 2).toFixed(1)}deg)`;
}

function rejectLovingAnswer(event, button) {
    event.preventDefault();
    event.stopPropagation();
    evade(button);
    button.animate(
        [
            { transform: button.style.transform || "translateX(0)" },
            { transform: "translateX(-8px)" },
            { transform: "translateX(8px)" },
            { transform: button.style.transform || "translateX(0)" }
        ],
        { duration: 260 }
    );
    const message = rejectionMessages[Math.floor(Math.random() * rejectionMessages.length)];
    showToast(message);
}

function showToast(message) {
    toast.textContent = message;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("show"), 2100);
}

function nextQuestion() {
    if (!questionAnswered) return;
    if (currentQuestion < questions.length - 1) {
        currentQuestion += 1;
        renderQuestion();
    } else {
        runReview();
    }
}

function runReview() {
    showScreen(reviewScreen);
    document.getElementById("scan-lines").innerHTML = "";
    document.getElementById("findings").classList.add("hidden");
    document.getElementById("system-error").classList.add("hidden");
    verdictBtn.classList.add("hidden");
    reviewTimers.forEach(clearTimeout);
    reviewTimers = [];

    scanMessages.forEach((message, index) => {
        const timer = setTimeout(() => {
            const line = document.createElement("div");
            line.className = "scan-line";
            line.textContent = message;
            document.getElementById("scan-lines").appendChild(line);
        }, index * 720);
        reviewTimers.push(timer);
    });

    reviewTimers.push(setTimeout(() => {
        document.getElementById("findings").classList.remove("hidden");
    }, scanMessages.length * 720 + 350));

    reviewTimers.push(setTimeout(() => {
        document.getElementById("system-error").classList.remove("hidden");
    }, scanMessages.length * 720 + 2150));

    reviewTimers.push(setTimeout(() => {
        verdictBtn.classList.remove("hidden");
        verdictBtn.scrollIntoView({ behavior: "smooth", block: "center" });
    }, scanMessages.length * 720 + 3900));
}

function showVerdict() {
    reviewTimers.forEach(clearTimeout);
    reviewTimers = [];
    sentenceBtn.classList.remove("hidden");
    courtSentenceSection.classList.add("hidden");
    showScreen(verdictScreen);
}

function showSentence() {
    sentenceBtn.classList.add("hidden");
    courtSentenceSection.classList.remove("hidden");
    launchConfetti();
    setTimeout(() => {
        courtSentenceSection.scrollIntoView({ behavior: "smooth", block: "start" });
    }, 180);
}

function launchConfetti() {
    const pieces = ["❤️", "💕", "💗", "✨", "🌸"];
    const count = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 12 : 85;
    for (let i = 0; i < count; i += 1) {
        const piece = document.createElement("span");
        piece.className = "confetti";
        piece.textContent = pieces[Math.floor(Math.random() * pieces.length)];
        piece.style.left = `${Math.random() * 100}vw`;
        piece.style.fontSize = `${14 + Math.random() * 20}px`;
        piece.style.animationDuration = `${3.7 + Math.random() * 3.4}s`;
        piece.style.animationDelay = `${Math.random() * 1.2}s`;
        document.body.appendChild(piece);
        setTimeout(() => piece.remove(), 8500);
    }
}

function addAmbientHearts() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    for (let i = 0; i < 12; i += 1) {
        const heart = document.createElement("span");
        heart.className = "floating-heart";
        heart.textContent = "♥";
        heart.style.left = `${Math.random() * 100}vw`;
        heart.style.fontSize = `${12 + Math.random() * 24}px`;
        heart.style.animationDuration = `${10 + Math.random() * 9}s`;
        heart.style.animationDelay = `${Math.random() * 12}s`;
        document.body.appendChild(heart);
    }
}

document.getElementById("start-btn").addEventListener("click", startQuiz);
nextBtn.addEventListener("click", nextQuestion);
verdictBtn.addEventListener("click", showVerdict);
sentenceBtn.addEventListener("click", showSentence);
document.getElementById("restart-btn").addEventListener("click", startQuiz);

addAmbientHearts();
</script>
</body>
</html>
"""


app_html = (
    HTML_TEMPLATE.replace("__PARTNER_NAME__", escape(PARTNER_NAME))
    .replace("__YOUR_NAME__", escape(YOUR_NAME))
)

components.html(app_html, height=1040, scrolling=True)
