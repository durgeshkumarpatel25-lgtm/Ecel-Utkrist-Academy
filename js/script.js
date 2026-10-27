/**
 * ECEL and Utkrist Computer Academy — Ambikapur
 * Spoken English & Computer Academy Vanilla JavaScript Engine
 */

document.addEventListener("DOMContentLoaded", () => {
  // ===========================================================================
  // 1. Mobile Hamburger Drawer & Animated Accordion
  // ===========================================================================
  const hamburgerBtn = document.getElementById("hamburgerBtn");
  const mobileDrawer = document.getElementById("mobileDrawer");
  const mobileDrawerOverlay = document.getElementById("mobileDrawerOverlay");
  const mobileDrawerClose = document.getElementById("mobileDrawerClose");
  const mobileNavLinks = document.querySelectorAll(".mobile-nav-link");

  function openMobileMenu() {
    if (mobileDrawer) mobileDrawer.classList.add("open");
    if (mobileDrawerOverlay) mobileDrawerOverlay.classList.add("open");
    if (hamburgerBtn) {
      hamburgerBtn.classList.add("is-active");
      hamburgerBtn.setAttribute("aria-expanded", "true");
    }
    document.body.style.overflow = "hidden";
  }

  function closeMobileMenu() {
    if (mobileDrawer) mobileDrawer.classList.remove("open");
    if (mobileDrawerOverlay) mobileDrawerOverlay.classList.remove("open");
    if (hamburgerBtn) {
      hamburgerBtn.classList.remove("is-active");
      hamburgerBtn.setAttribute("aria-expanded", "false");
    }
    document.body.style.overflow = "";
  }

  // Expose to window for global invocation (modals / buttons)
  window.openMobileMenu = openMobileMenu;
  window.closeMobileMenu = closeMobileMenu;

  if (hamburgerBtn) {
    hamburgerBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      if (mobileDrawer && mobileDrawer.classList.contains("open")) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
  }

  if (mobileDrawerClose) mobileDrawerClose.addEventListener("click", closeMobileMenu);
  if (mobileDrawerOverlay) mobileDrawerOverlay.addEventListener("click", closeMobileMenu);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && mobileDrawer && mobileDrawer.classList.contains("open")) {
      closeMobileMenu();
    }
  });

  mobileNavLinks.forEach((link) => {
    link.addEventListener("click", () => {
      mobileNavLinks.forEach((l) => l.classList.remove("active"));
      link.classList.add("active");
      closeMobileMenu();
    });
  });

  // Mobile Drawer Accordion Toggles (Registration & Test Paper)
  // Submenus stay closed by default and smoothly animate on tap
  const mobileAccordionPairs = [
    { btnId: "mobileRegBtn", submenuId: "mobileRegSubmenu" },
    { btnId: "mobileTestPaperBtn", submenuId: "mobileTestPaperSubmenu" }
  ];

  mobileAccordionPairs.forEach(({ btnId, submenuId }) => {
    const btn = document.getElementById(btnId);
    const submenu = document.getElementById(submenuId);
    if (btn && submenu) {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        const willOpen = !submenu.classList.contains("open");

        // Close other accordion for clean single-expanded view
        mobileAccordionPairs.forEach((other) => {
          if (other.btnId !== btnId) {
            const otherBtn = document.getElementById(other.btnId);
            const otherSub = document.getElementById(other.submenuId);
            if (otherSub) otherSub.classList.remove("open");
            if (otherBtn) {
              otherBtn.classList.remove("open");
              otherBtn.setAttribute("aria-expanded", "false");
            }
          }
        });

        // Toggle current accordion
        if (willOpen) {
          submenu.classList.add("open");
          btn.classList.add("open");
          btn.setAttribute("aria-expanded", "true");
        } else {
          submenu.classList.remove("open");
          btn.classList.remove("open");
          btn.setAttribute("aria-expanded", "false");
        }
      });
    }
  });

  // Close mobile drawer when clicking on any subnav link
  const mobileSubnavLinks = document.querySelectorAll(".mobile-subnav-link");
  mobileSubnavLinks.forEach((sublink) => {
    sublink.addEventListener("click", () => {
      closeMobileMenu();
    });
  });

  // Desktop Dropdown Toggles for click/touch devices (Registration & Test Paper)
  const dropdownPairs = [
    { dropdownId: "desktopRegDropdown", btnId: "regDropdownBtn" },
    { dropdownId: "desktopTestPaperDropdown", btnId: "testPaperDropdownBtn" }
  ];

  dropdownPairs.forEach(({ dropdownId, btnId }) => {
    const dropdown = document.getElementById(dropdownId);
    const btn = document.getElementById(btnId);
    if (dropdown && btn) {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        // Close other dropdowns
        dropdownPairs.forEach((other) => {
          if (other.dropdownId !== dropdownId) {
            const otherEl = document.getElementById(other.dropdownId);
            const otherBtn = document.getElementById(other.btnId);
            if (otherEl) otherEl.classList.remove("open");
            if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
          }
        });
        const isOpen = dropdown.classList.toggle("open");
        btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
      });
    }
  });

  document.addEventListener("click", (e) => {
    dropdownPairs.forEach(({ dropdownId, btnId }) => {
      const dropdown = document.getElementById(dropdownId);
      const btn = document.getElementById(btnId);
      if (dropdown && !dropdown.contains(e.target)) {
        dropdown.classList.remove("open");
        if (btn) btn.setAttribute("aria-expanded", "false");
      }
    });
  });

  // ===========================================================================
  // 2. Sticky Header & Active Nav ScrollSpy
  // ===========================================================================
  const header = document.querySelector(".header");
  const navLinks = document.querySelectorAll(".nav-link");
  const sections = document.querySelectorAll("section[id]");

  window.addEventListener("scroll", () => {
    if (header) {
      if (window.scrollY > 30) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }
    }

    // ScrollSpy
    const scrollPos = window.scrollY + 220;
    sections.forEach((section) => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute("id");

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach((link) => {
          link.classList.remove("active");
          if (link.getAttribute("href") === `#${id}`) {
            link.classList.add("active");
          }
        });
      }
    });
  }, { passive: true });

  // ===========================================================================
  // 3. Demo Modal Trigger & Pre-selection
  // ===========================================================================
  const demoModal = document.getElementById("demoModal");
  const modalCloseBtn = document.getElementById("modalCloseBtn");
  const modalCourseSelect = document.getElementById("modalCourseInterested");
  const openDemoButtons = document.querySelectorAll(".open-demo-modal");

  window.openDemoModal = function (courseName) {
    if (typeof closeMobileMenu === "function") {
      closeMobileMenu();
    }
    if (courseName && modalCourseSelect) {
      for (let i = 0; i < modalCourseSelect.options.length; i++) {
        if (modalCourseSelect.options[i].text.toLowerCase().includes(courseName.toLowerCase()) ||
          modalCourseSelect.options[i].value.toLowerCase().includes(courseName.toLowerCase())) {
          modalCourseSelect.selectedIndex = i;
          break;
        }
      }
    }
    if (demoModal) {
      demoModal.classList.add("open");
      document.body.style.overflow = "hidden";
    }
  };

  window.closeDemoModal = function () {
    if (demoModal) {
      demoModal.classList.remove("open");
      document.body.style.overflow = "";
    }
  };

  openDemoButtons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const course = btn.getAttribute("data-course") || "";
      window.openDemoModal(course);
    });
  });

  if (modalCloseBtn) modalCloseBtn.addEventListener("click", window.closeDemoModal);

  if (demoModal) {
    demoModal.addEventListener("click", (e) => {
      if (e.target === demoModal) {
        window.closeDemoModal();
      }
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && demoModal && demoModal.classList.contains("open")) {
      window.closeDemoModal();
    }
  });

  // ===========================================================================
  // 4. Form Validation & WhatsApp Confirmation
  // ===========================================================================
  function setupDemoForm(formId, successBoxId) {
    const form = document.getElementById(formId);
    const successBox = document.getElementById(successBoxId);

    if (!form) return;

    form.addEventListener("submit", (e) => {
      e.preventDefault();

      const fullName = form.querySelector('[name="fullName"]').value.trim();
      const phone = form.querySelector('[name="phone"]').value.trim();
      const course = form.querySelector('[name="courseInterested"]').value;
      const level = form.querySelector('[name="currentLevel"]').value;
      const time = form.querySelector('[name="preferredTime"]').value;
      const message = form.querySelector('[name="message"]') ? form.querySelector('[name="message"]').value.trim() : "";
      const honeypot = form.querySelector('[name="honeypot"]') ? form.querySelector('[name="honeypot"]').value : "";
      const submitBtn = form.querySelector('button[type="submit"]');

      // Honeypot spam check
      if (honeypot && honeypot.length > 0) {
        return;
      }

      // Name Validation
      if (fullName.length < 2) {
        alert("Please enter your full name (minimum 2 characters).");
        return;
      }

      // 10-digit Indian mobile validation
      const indianPhoneRegex = /^[6-9]\d{9}$/;
      if (!indianPhoneRegex.test(phone)) {
        alert("Please enter a valid 10-digit Indian mobile number (e.g. 8962469909).");
        return;
      }

      // Loading state
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = "<span>Reserving Your Slot...</span>";

      // Payload
      const leadPayload = {
        fullName,
        phone,
        courseInterested: course,
        currentLevel: level,
        preferredTime: time,
        message,
        source: formId === "modalDemoForm" ? "Popup Modal" : "Page Section",
        submittedAt: new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }),
      };

      console.log("📥 Lead Submitted:", leadPayload);

      // Simulate API submission
      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
        form.style.display = "none";

        if (successBox) {
          successBox.style.display = "block";
          const studentNameEl = successBox.querySelector(".student-name-display");
          const whatsappConfirmBtn = successBox.querySelector(".whatsapp-confirm-link");

          if (studentNameEl) studentNameEl.textContent = fullName;

          if (whatsappConfirmBtn) {
            const courseEmojis = {
              "Advance Spoken English (Morning Batch)": "🌅 (Morning Fluency & Speaking)",
              "Advance Spoken English (Evening Batch)": "🌇 (Evening Fluency & Speaking)",
              "Advanced Fluency & Public Speaking": "🎙️ (Fluency, Extempore & Public Speaking)",
              "Complete Advance English Course": "🌟 (6-Month Complete Fluency & Personality)",
              "DCA (Diploma in Computer Application)": "💻 (DCA - 1 Year Diploma)",
              "PGDCA (Post Graduate Diploma in Computer Application)": "🎓 (PGDCA - Post Graduate Diploma)",
              "Basic Computer Course (BCC)": "🖥️ (Basic Computer, Typing & MS Office)",
              "Tally Prime with GST & Accounting": "📊 (Tally Prime, GST, Invoicing & Payroll)"
            };

            const courseBadge = courseEmojis[course] || "📖";

            const richEmojiMessage =
              `👋 *नमस्ते Sir / Team ECEL & Utkrist Computer Academy!*\n\n` +
              `🎯 *New Free Demo Class Registration*\n` +
              `━━━━━━━━━━━━━━━━━━━━━━\n` +
              `👤 *Student Name:* ${fullName}\n` +
              `📱 *Mobile Number:* +91 ${phone}\n` +
              `📚 *Course Interested:* ${course}\n` +
              `   ↳ ${courseBadge}\n` +
              `📊 *Current Level:* ${level} 📈\n` +
              `⏰ *Preferred Batch Time:* ${time} ⏳\n` +
              (message ? `💬 *Student Goal / Note:* "${message}" 🚀\n` : `💬 *Goal:* Learn Spoken English & Computer Skills with Confidence! 🚀\n`) +
              `📍 *Campus:* Banaras Road, Near Mishra Sweets, RG Tower, Ambikapur (CG) 497001\n` +
              `━━━━━━━━━━━━━━━━━━━━━━\n` +
              `🙏 *Please confirm my free demo seat & timing!* ✨🌟`;

            const encodedMsg = encodeURIComponent(richEmojiMessage);
            whatsappConfirmBtn.setAttribute("href", `https://wa.me/918962469909?text=${encodedMsg}`);
          }
        }

        // Trigger Canvas Confetti
        fireConfetti();
      }, 700);
    });
  }

  setupDemoForm("inlineDemoForm", "inlineSuccessBox");
  setupDemoForm("modalDemoForm", "modalSuccessBox");

  // ===========================================================================
  // 5. FAQ Accordion
  // ===========================================================================
  const faqItems = document.querySelectorAll(".faq-item");

  faqItems.forEach((item) => {
    const questionBtn = item.querySelector(".faq-question");
    if (!questionBtn) return;

    questionBtn.addEventListener("click", () => {
      const isActive = item.classList.contains("active");

      // Close all other FAQs for clean single-accordion UX
      faqItems.forEach((other) => other.classList.remove("active"));

      if (!isActive) {
        item.classList.add("active");
      }
    });
  });

  // ===========================================================================
  // 6. Animated Stats Counter
  // ===========================================================================
  const statNumbers = document.querySelectorAll(".stat-number[data-target]");
  let statsCounted = false;

  function countUp(el) {
    const target = parseInt(el.getAttribute("data-target"), 10);
    const suffix = el.getAttribute("data-suffix") || "";
    const duration = 1600;
    const stepTime = 30;
    const steps = duration / stepTime;
    const increment = target / steps;
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        el.innerHTML = `${target}<span>${suffix}</span>`;
        clearInterval(timer);
      } else {
        el.innerHTML = `${Math.floor(current)}<span>${suffix}</span>`;
      }
    }, stepTime);
  }

  const statsSection = document.getElementById("statsStrip");
  if (statsSection) {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting && !statsCounted) {
        statsCounted = true;
        statNumbers.forEach(countUp);
      }
    }, { threshold: 0.25 });
    observer.observe(statsSection);
  }

  // ===========================================================================
  // 7. Confetti Effect (Pure Vanilla Canvas)
  // ===========================================================================
  function fireConfetti() {
    const canvas = document.createElement("canvas");
    canvas.style.position = "fixed";
    canvas.style.top = "0";
    canvas.style.left = "0";
    canvas.style.width = "100%";
    canvas.style.height = "100%";
    canvas.style.pointerEvents = "none";
    canvas.style.zIndex = "999";
    document.body.appendChild(canvas);

    const ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ["#F59E0B", "#1E3A8A", "#10B981", "#3B82F6", "#EF4444"];

    for (let i = 0; i < 60; i++) {
      particles.push({
        x: canvas.width / 2,
        y: canvas.height * 0.6,
        r: Math.random() * 6 + 4,
        dx: (Math.random() - 0.5) * 12,
        dy: (Math.random() - 0.7) * 14,
        color: colors[Math.floor(Math.random() * colors.length)],
        tilt: Math.random() * 10,
        tiltAngle: Math.random() * Math.PI,
      });
    }

    let animationFrame;
    let opacity = 1;

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.globalAlpha = opacity;

      particles.forEach((p) => {
        p.x += p.dx;
        p.y += p.dy;
        p.dy += 0.25; // gravity
        p.tiltAngle += 0.1;

        ctx.beginPath();
        ctx.fillStyle = p.color;
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      });

      opacity -= 0.015;
      if (opacity > 0) {
        animationFrame = requestAnimationFrame(render);
      } else {
        cancelAnimationFrame(animationFrame);
        canvas.remove();
      }
    }

    render();
  }

  // ===========================================================================
  // 8. Timed / Exit Intent Offer Popup
  // ===========================================================================
  const exitOffer = document.getElementById("exitOfferBanner");
  const closeExitOffer = document.getElementById("closeExitOffer");

  if (exitOffer) {
    const alreadyShown = sessionStorage.getItem("demo_offer_shown");
    if (!alreadyShown) {
      setTimeout(() => {
        if (!sessionStorage.getItem("demo_offer_shown")) {
          exitOffer.style.display = "block";
          sessionStorage.setItem("demo_offer_shown", "true");
        }
      }, 20000);

      document.addEventListener("mouseleave", (e) => {
        if (e.clientY <= 10 && !sessionStorage.getItem("demo_offer_shown")) {
          exitOffer.style.display = "block";
          sessionStorage.setItem("demo_offer_shown", "true");
        }
      });
    }

    if (closeExitOffer) {
      closeExitOffer.addEventListener("click", () => {
        exitOffer.style.display = "none";
      });
    }
  }

  // ===========================================================================
  // 9. Interactive 60-Sec English Hesitation Quiz Engine
  // ===========================================================================
  let quizScores = { 1: 0, 2: 0, 3: 0 };

  window.handleQuizAnswer = function (step, score) {
    quizScores[step] = score;

    const progress = document.getElementById("quizProgressBar");
    const step1 = document.getElementById("quizStep1");
    const step2 = document.getElementById("quizStep2");
    const step3 = document.getElementById("quizStep3");
    const resultCard = document.getElementById("quizResultCard");

    if (step === 1) {
      if (step1) step1.style.display = "none";
      if (step2) step2.style.display = "block";
      if (progress) progress.style.width = "66%";
    } else if (step === 2) {
      if (step2) step2.style.display = "none";
      if (step3) step3.style.display = "block";
      if (progress) progress.style.width = "100%";
    } else if (step === 3) {
      if (step3) step3.style.display = "none";
      if (resultCard) resultCard.style.display = "block";

      const totalScore = quizScores[1] + quizScores[2] + quizScores[3];
      const headlineEl = document.getElementById("quizResultHeadline");
      const meterBarEl = document.getElementById("resultMeterBar");
      const descEl = document.getElementById("quizResultDesc");
      const waActionEl = document.getElementById("quizWhatsappAction");

      let headline = "";
      let meterPercent = totalScore;
      let diagnosis = "";
      let recommendedCourse = "";

      if (totalScore >= 65) {
        headline = `${totalScore}% Hesitation Detected — "Translation Loop & Stage Freeze"`;
        meterPercent = Math.min(totalScore, 95);
        diagnosis = "आप अंग्रेजी समझ लेते हैं, लेकिन दिमाग में वाक्य हिंदी-से-अंग्रेजी अनुवाद में अटक जाते हैं और माइक के सामने घबराहट होती है। हमारे 20-मिनट के डेली पोडियम माइक अभ्यास से आप 30-45 दिनों में इस झिझक को पूरी तरह तोड़ सकते हैं!";
        recommendedCourse = "Advance Spoken English (Morning / Evening) + Stage Mic Drills";
      } else if (totalScore >= 35) {
        headline = `${totalScore}% Hesitation Detected — "Vocabulary & Continuity Gap"`;
        meterPercent = Math.max(totalScore, 45);
        diagnosis = "आप सामान्य बातचीत कर लेते हैं, लेकिन बीच में सही शब्द (Vocabulary) भूल जाते हैं और 10 मिनट लगातार नहीं बोल पाते। हमारे डिबेट एरिना एवं एक्सटेम्पोर ड्रिल्स से आपको धाराप्रवाह प्रवाह मिलेगा!";
        recommendedCourse = "Advanced Spoken English & Fluency Mastery";
      } else {
        headline = `${Math.max(totalScore, 20)}% Hesitation — "Executive Polish & Placement Ready"`;
        meterPercent = Math.max(totalScore, 25);
        diagnosis = "आपके पास बोलने का अच्छा आत्मविश्वास है! आपको केवल एग्जीक्यूटिव ग्रूमिंग, कॉर्पोरेट इंटरव्यू तैयारी, और बॉडी लैंग्वेज पॉलिश की आवश्यकता है ताकि आप किसी भी MNC और कॉम्पिटिटिव इंटरव्यू में अव्वल आ सकें!";
        recommendedCourse = "Public Speaking & Interview Mastery";
      }

      if (headlineEl) headlineEl.textContent = headline;
      if (meterBarEl) meterBarEl.style.width = `${meterPercent}%`;
      if (descEl) descEl.textContent = diagnosis;

      if (waActionEl) {
        const richMsg =
          `👋 *नमस्ते Sir / Team ECEL & Utkrist Computer Academy!*\n\n` +
          `🎯 *I completed the English Hesitation Test on your website!*\n` +
          `━━━━━━━━━━━━━━━━━━━━━━\n` +
          `📊 *My Test Result:* ${headline}\n` +
          `💡 *Diagnosis:* "${diagnosis}"\n` +
          `📚 *Recommended Course:* ${recommendedCourse} 🚀\n` +
          `📍 *Campus:* Banaras Road, Near Mishra Sweets, RG Tower, Ambikapur (CG)\n` +
          `━━━━━━━━━━━━━━━━━━━━━━\n` +
          `🙏 *Please confirm when I can attend my Free 1-on-1 Hesitation Diagnosis Session!* ✨🌟`;

        waActionEl.setAttribute("href", `https://wa.me/918962469909?text=${encodeURIComponent(richMsg)}`);
      }
    }
  };

  window.resetQuiz = function () {
    quizScores = { 1: 0, 2: 0, 3: 0 };
    const step1 = document.getElementById("quizStep1");
    const step2 = document.getElementById("quizStep2");
    const step3 = document.getElementById("quizStep3");
    const resultCard = document.getElementById("quizResultCard");
    const progress = document.getElementById("quizProgressBar");

    if (resultCard) resultCard.style.display = "none";
    if (step3) step3.style.display = "none";
    if (step2) step2.style.display = "none";
    if (step1) step1.style.display = "block";
    if (progress) progress.style.width = "33%";
  };

  // ===========================================================================
  // 10. Scroll Reveal Animation Observer (Ultra-Fast 60fps)
  // ===========================================================================
  const revealElements = document.querySelectorAll(".reveal-on-scroll");
  if (revealElements.length > 0 && "IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: "0px 0px -50px 0px",
      threshold: 0.12
    });

    revealElements.forEach((el) => revealObserver.observe(el));
  } else {
    // Fallback if IntersectionObserver is not supported
    revealElements.forEach((el) => el.classList.add("revealed"));
  }

  // ===========================================================================
  // 11. Image Lightbox System (Optional Click-to-Zoom)
  // ===========================================================================
  const bannerLightbox = document.getElementById("bannerLightbox");
  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxCloseBtn = document.getElementById("lightboxCloseBtn");

  window.openBannerLightbox = function (imageSrc) {
    if (bannerLightbox && lightboxImg) {
      lightboxImg.src = imageSrc;
      bannerLightbox.classList.add("open");
      document.body.style.overflow = "hidden";
    }
  };

  window.closeBannerLightbox = function () {
    if (bannerLightbox) {
      bannerLightbox.classList.remove("open");
      document.body.style.overflow = "";
    }
  };

  if (lightboxCloseBtn) {
    lightboxCloseBtn.addEventListener("click", window.closeBannerLightbox);
  }

  if (bannerLightbox) {
    bannerLightbox.addEventListener("click", (e) => {
      if (e.target === bannerLightbox) {
        window.closeBannerLightbox();
      }
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && bannerLightbox && bannerLightbox.classList.contains("open")) {
      window.closeBannerLightbox();
    }
  });

  // ===========================================================================
  // 12. Course Category Filter Bar (All, Spoken English, Utkrist Computer Academy)
  // ===========================================================================
  const courseFilterBtns = document.querySelectorAll(".course-filter-btn");
  const allCourseCards = document.querySelectorAll(".course-card[data-category]");

  courseFilterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const filterValue = btn.getAttribute("data-filter");

      // Update active button
      courseFilterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      // Show/Hide Course Cards
      allCourseCards.forEach((card) => {
        const cardCategory = card.getAttribute("data-category");
        if (filterValue === "all" || cardCategory === filterValue) {
          card.style.display = "flex";
          card.classList.add("revealed");
        } else {
          card.style.display = "none";
        }
      });
    });
  });
});