// =============================================
// AGUINACO AERIALS — Main JavaScript v2.1
// =============================================

(function () {
  'use strict';

  // Configura tu endpoint Formspree: https://formspree.io/
  const FORM_ENDPOINT = document.querySelector('#contactForm')?.dataset.endpoint || '';

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

  document.addEventListener('DOMContentLoaded', () => {

    // ─────────────────────────────────────────
    // NAVBAR SCROLL BEHAVIOUR
    // ─────────────────────────────────────────
    const navbar = $('#navbar');
    if (navbar) {
      const onScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 48);
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }

    // ─────────────────────────────────────────
    // ACTIVE NAV LINK
    // ─────────────────────────────────────────
    const currentPath = window.location.pathname.replace(/\/$/, '');
    $$('.nav-links a').forEach(link => {
      const href = link.getAttribute('href');
      if (href && href !== '#' && currentPath.includes(href.replace('.html', ''))) {
        link.classList.add('active');
      }
    });

    // ─────────────────────────────────────────
    // MOBILE MENU
    // ─────────────────────────────────────────
    const hamburger = $('#hamburger');
    const mobileMenu = $('#mobileMenu');
    const mobileClose = $('#mobileClose');

    function setMenuExpanded(isOpen) {
      hamburger?.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      hamburger?.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
    }

    function openMobileMenu() {
      mobileMenu?.classList.add('open');
      hamburger?.classList.add('open');
      document.body.style.overflow = 'hidden';
      setMenuExpanded(true);
      mobileClose?.focus();
    }

    function closeMobileMenu() {
      mobileMenu?.classList.remove('open');
      hamburger?.classList.remove('open');
      document.body.style.overflow = '';
      setMenuExpanded(false);
      hamburger?.focus();
    }

    hamburger?.addEventListener('click', () => {
      mobileMenu?.classList.contains('open') ? closeMobileMenu() : openMobileMenu();
    });

    mobileClose?.addEventListener('click', closeMobileMenu);

    $$('.mobile-nav-link, .mobile-menu .btn').forEach(el =>
      el.addEventListener('click', closeMobileMenu)
    );

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        closeMobileMenu();
        closeModal();
        closeCookieBanner();
      }
    });

    // ─────────────────────────────────────────
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ─────────────────────────────────────────
    $$('a[href^="#"]').forEach(link => {
      link.addEventListener('click', e => {
        const id = link.getAttribute('href');
        if (id === '#') return;
        const target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          const offset = navbar ? navbar.offsetHeight + 16 : 80;
          window.scrollTo({
            top: target.getBoundingClientRect().top + window.scrollY - offset,
            behavior: 'smooth'
          });
        }
      });
    });

    // ─────────────────────────────────────────
    // SCROLL REVEAL
    // ─────────────────────────────────────────
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
      $$('.fade-up, .fade-in').forEach(el => el.classList.add('visible'));
    } else {
      const io = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const parent = el.parentElement;
          const siblings = $$(':scope > .fade-up', parent);
          const idx = siblings.indexOf(el);
          const delay = Math.min(idx * 90, 450);
          setTimeout(() => el.classList.add('visible'), delay);
          io.unobserve(el);
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

      $$('.fade-up, .fade-in').forEach(el => io.observe(el));
    }

    // ─────────────────────────────────────────
    // PORTFOLIO FILTER TABS
    // ─────────────────────────────────────────
    const tabs = $$('.portfolio-tab');
    const portfolioItems = $$('.portfolio-item');

    if (tabs.length && portfolioItems.length) {
      portfolioItems.forEach(item => {
        item.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
      });

      tabs.forEach((tab, index) => {
        if (!tab.id) tab.id = `portfolio-tab-${index}`;
        tab.setAttribute('aria-controls', 'portfolio-grid');

        tab.addEventListener('click', () => {
          tabs.forEach(t => {
            t.classList.remove('active');
            t.setAttribute('aria-selected', 'false');
          });
          tab.classList.add('active');
          tab.setAttribute('aria-selected', 'true');

          const filter = tab.dataset.filter;
          portfolioItems.forEach(item => {
            const match = filter === 'all' || item.dataset.category === filter;
            if (match) {
              item.style.display = '';
              item.hidden = false;
              requestAnimationFrame(() => {
                item.style.opacity = '1';
                item.style.transform = 'scale(1)';
              });
            } else {
              item.style.opacity = '0';
              item.style.transform = 'scale(0.94)';
              setTimeout(() => {
                const activeFilter = document.querySelector('.portfolio-tab.active')?.dataset.filter;
                if (item.dataset.category !== activeFilter && activeFilter !== 'all') {
                  item.style.display = 'none';
                  item.hidden = true;
                }
              }, 380);
            }
          });
        });
      });

      const grid = $('.portfolio-grid');
      if (grid && !grid.id) grid.id = 'portfolio-grid';
    }

    // ─────────────────────────────────────────
    // FAQ ACCORDION
    // ─────────────────────────────────────────
    const faqItems = $$('.faq-item');
    faqItems.forEach(item => {
      const question = $('.faq-question', item);
      const answer = $('.faq-answer', item);
      if (!question || !answer) return;

      question.addEventListener('click', () => {
        const isOpen = item.classList.contains('active');

        faqItems.forEach(other => {
          other.classList.remove('active');
          const q = $('.faq-question', other);
          const ans = $('.faq-answer', other);
          if (q) q.setAttribute('aria-expanded', 'false');
          if (ans) ans.style.maxHeight = null;
        });

        if (!isOpen) {
          item.classList.add('active');
          question.setAttribute('aria-expanded', 'true');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      });
    });

    // ─────────────────────────────────────────
    // CONTACT FORM
    // ─────────────────────────────────────────
    const form = $('#contactForm');
    const submitBtn = $('#submitBtn');
    const formMsg = $('#formMessage');

    if (form) {
      form.addEventListener('submit', async e => {
        e.preventDefault();

        const name = $('#name')?.value.trim();
        const email = $('#email')?.value.trim();
        const message = $('#message')?.value.trim();
        const privacy = $('#privacy')?.checked;

        if (!name || !email || !message) {
          showFormMsg('Por favor, rellena todos los campos obligatorios.', 'error');
          return;
        }
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
          showFormMsg('Por favor, introduce un email válido.', 'error');
          return;
        }
        if (!privacy) {
          showFormMsg('Debes aceptar la Política de privacidad para continuar.', 'error');
          return;
        }

        if (submitBtn) {
          submitBtn.textContent = 'Enviando…';
          submitBtn.disabled = true;
        }

        const endpoint = form.dataset.endpoint || FORM_ENDPOINT;

        try {
          if (endpoint) {
            const formData = new FormData(form);
            const response = await fetch(endpoint, {
              method: 'POST',
              body: formData,
              headers: { Accept: 'application/json' }
            });

            if (!response.ok) throw new Error('Error al enviar');

            showFormMsg('¡Mensaje enviado! Te respondo en menos de 24 horas.', 'success');
            form.reset();
          } else {
            const phone = $('#phone')?.value.trim() || '';
            const service = $('#service')?.value || '';
            const company = $('#company')?.value.trim() || '';
            const subject = encodeURIComponent(`Consulta web — ${name}`);
            const body = encodeURIComponent(
              `Nombre: ${name}\nEmail: ${email}\nTeléfono: ${phone}\nEmpresa: ${company}\nServicio: ${service}\n\n${message}`
            );
            window.location.href = `mailto:info@aguinacoaerials.com?subject=${subject}&body=${body}`;
            showFormMsg('Se abrirá tu cliente de correo para enviar la consulta.', 'success');
          }
        } catch (err) {
          showFormMsg('No se pudo enviar el mensaje. Llama al +34 685 09 75 04 o escribe a info@aguinacoaerials.com.', 'error');
        } finally {
          if (submitBtn) {
            submitBtn.textContent = 'Enviar mensaje';
            submitBtn.disabled = false;
          }
        }
      });
    }

    function showFormMsg(text, type) {
      if (!formMsg) return;
      formMsg.textContent = text;
      formMsg.className = 'form-msg';
      formMsg.style.display = 'block';
      if (type === 'success') {
        formMsg.style.background = 'rgba(34,197,94,0.1)';
        formMsg.style.border = '1px solid rgba(34,197,94,0.25)';
        formMsg.style.color = '#4ade80';
      } else {
        formMsg.style.background = 'rgba(239,68,68,0.1)';
        formMsg.style.border = '1px solid rgba(239,68,68,0.25)';
        formMsg.style.color = '#f87171';
      }
      setTimeout(() => { formMsg.style.display = 'none'; }, 8000);
    }

    // ─────────────────────────────────────────
    // MODAL
    // ─────────────────────────────────────────
    const modalOverlay = $('#modalOverlay');
    const modalClose = $('#modalClose');

    function openModal() {
      if (modalOverlay) {
        modalOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeModal() {
      if (modalOverlay) {
        modalOverlay.classList.remove('open');
        document.body.style.overflow = '';
      }
    }

    modalClose?.addEventListener('click', closeModal);
    modalOverlay?.addEventListener('click', e => {
      if (e.target === modalOverlay) closeModal();
    });

    window.AA = { openModal, closeModal };

    // ─────────────────────────────────────────
    // PARALLAX HERO (disabled on reduced motion / mobile)
    // ─────────────────────────────────────────
    const heroVideo = $('#heroBgVideo');
    if (heroVideo && !prefersReducedMotion && window.innerWidth > 960) {
      window.addEventListener('scroll', () => {
        heroVideo.style.transform = `translateY(${window.scrollY * 0.25}px)`;
      }, { passive: true });
    }

    // Pause hero video when tab hidden (save resources)
    if (heroVideo) {
      document.addEventListener('visibilitychange', () => {
        if (document.hidden) heroVideo.pause();
        else heroVideo.play().catch(() => {});
      });
    }

    // ─────────────────────────────────────────
    // HERO SCROLL INDICATOR
    // ─────────────────────────────────────────
    const scrollIndicator = $('#heroScrollIndicator');
    if (scrollIndicator) {
      const scrollToNext = () => {
        const next = document.querySelector('#services') || document.querySelector('.section');
        if (next) next.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth' });
      };
      scrollIndicator.addEventListener('click', scrollToNext);
      scrollIndicator.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          scrollToNext();
        }
      });
    }

    // ─────────────────────────────────────────
    // COOKIE BANNER
    // ─────────────────────────────────────────
    const cookieBanner = $('#cookieBanner');
    const cookieAccept = $('#cookieAccept');
    const cookieReject = $('#cookieReject');

    function closeCookieBanner() {
      if (cookieBanner) cookieBanner.style.display = 'none';
    }

    if (cookieBanner && !localStorage.getItem('aa_cookies')) {
      setTimeout(() => {
        cookieBanner.style.display = 'flex';
        if (!prefersReducedMotion) {
          cookieBanner.style.animation = 'cookieIn 0.4s ease forwards';
        }
      }, 2000);
    }

    cookieAccept?.addEventListener('click', () => {
      localStorage.setItem('aa_cookies', 'accepted');
      closeCookieBanner();
    });

    cookieReject?.addEventListener('click', () => {
      localStorage.setItem('aa_cookies', 'rejected');
      closeCookieBanner();
    });

    // ─────────────────────────────────────────
    // COUNTER ANIMATION
    // ─────────────────────────────────────────
    const counters = $$('[data-count]');
    if (counters.length && !prefersReducedMotion) {
      const counterObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const target = parseFloat(el.dataset.count);
          const suffix = el.dataset.suffix || '';
          const prefix = el.dataset.prefix || '';
          const duration = 1800;
          const start = performance.now();

          function update(now) {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const value = Math.round(eased * target * 10) / 10;
            el.textContent = prefix + (Number.isInteger(target) ? Math.round(value) : value) + suffix;
            if (progress < 1) requestAnimationFrame(update);
          }

          requestAnimationFrame(update);
          counterObserver.unobserve(el);
        });
      }, { threshold: 0.5 });

      counters.forEach(el => counterObserver.observe(el));
    }

  });

})();
