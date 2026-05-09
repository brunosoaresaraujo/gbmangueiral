// Reveal Animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // Only animate once
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal, .text-clip-anim').forEach(el => observer.observe(el));

// Parallax & Navbar Scroll
const parallaxBg = document.getElementById('parallax-bg');
const nav = document.getElementById('main-nav');

window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;

  // Parallax Background
  if (parallaxBg) {
    parallaxBg.style.transform = `translateY(${scrolled * 0.4}px)`;
  }

  // Navbar Styling
  if (scrolled > 50) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
});

// Flashlight Hover Effect Pattern (Styleguide)
document.querySelectorAll('.hero-float-card, .prof-card, .time-slot, .benefit-card, .legacy-feat-item, .contact-card, .stat-pill').forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
    card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
  });
});

// Video Slider Logic
const videos = document.querySelectorAll('.slide-video');
const indicators = document.querySelectorAll('.slide-indicator');
const fills = [document.getElementById('prog-1'), document.getElementById('prog-2'), document.getElementById('prog-3')];
let currentSlide = 0;

function switchSlide(index) {
  if (index === currentSlide) return;

  videos[currentSlide].classList.remove('active');
  indicators[currentSlide].classList.remove('active');
  fills[currentSlide].style.width = '0%';

  // Use setTimeout to pause after fade out
  const prevVideo = videos[currentSlide];
  setTimeout(() => { prevVideo.pause(); prevVideo.currentTime = 0; }, 1500);

  currentSlide = index;

  videos[currentSlide].classList.add('active');
  indicators[currentSlide].classList.add('active');
  videos[currentSlide].play();
}

videos.forEach((vid, idx) => {
  vid.addEventListener('timeupdate', () => {
    if (idx === currentSlide && vid.duration) {
      const percent = (vid.currentTime / vid.duration) * 100;
      fills[idx].style.width = `${percent}%`;
    }
  });
  vid.addEventListener('ended', () => {
    let next = (currentSlide + 1) % videos.length;
    switchSlide(next);
  });
});

indicators.forEach((ind, idx) => {
  ind.addEventListener('click', () => {
    switchSlide(idx);
  });
});

// Ensure first video plays on load
videos[0].play().catch(e => console.log("Autoplay prevented:", e));

// Professor Slider Logic
const profSlider = document.getElementById('prof-slider');
const profPrev = document.getElementById('prof-prev');
const profNext = document.getElementById('prof-next');

if (profSlider && profPrev && profNext) {
  const scrollAmount = 450;

  const nextSlide = () => {
    const maxScroll = profSlider.scrollWidth - profSlider.clientWidth;
    if (profSlider.scrollLeft >= maxScroll - 10) {
      profSlider.scrollTo({ left: 0, behavior: 'smooth' });
    } else {
      profSlider.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
  };

  const prevSlide = () => {
    if (profSlider.scrollLeft <= 10) {
      profSlider.scrollTo({ left: profSlider.scrollWidth, behavior: 'smooth' });
    } else {
      profSlider.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    }
  };

  profNext.addEventListener('click', nextSlide);
  profPrev.addEventListener('click', prevSlide);

  // Professor Video Hover Logic
  document.querySelectorAll('.prof-card').forEach(card => {
    const video = card.querySelector('video');
    if (video) {
      card.addEventListener('mouseenter', () => {
        video.play().catch(e => console.log("Playback failed:", e));
      });
      card.addEventListener('mouseleave', () => {
        video.pause();
      });
    }
  });
}

// Schedule Tab Logic
const dayTabs = document.querySelectorAll('.day-tab');
const dayContents = document.querySelectorAll('.day-content');

dayTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const targetDay = tab.getAttribute('data-day');

    // Update Tabs
    dayTabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    // Update Content
    dayContents.forEach(content => {
      content.classList.remove('active');
      if (content.id === targetDay) {
        content.classList.add('active');
      }
    });
  });
});
