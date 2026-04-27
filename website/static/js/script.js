// Mobile menu toggle
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');

menuToggle.addEventListener('click', () => {
  menuToggle.classList.toggle('active');
  navLinks.classList.toggle('active');
  navLinks.classList.toggle("display")
});

// Close mobile menu when a link is clicked
const navItems = document.querySelectorAll('.nav-link');
navItems.forEach(item => {
  item.addEventListener('click', () => {
    menuToggle.classList.remove('active');
    navLinks.classList.remove('active');
    
    navItems.forEach(link => link.classList.remove('active'));
    item.classList.add('active');
  });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.navbar') && !e.target.closest('.nav-links')) {
    menuToggle.classList.remove('active');
    navLinks.classList.remove('active');
  }
});

// Smooth scroll behavior
document.documentElement.style.scrollBehavior = 'smooth';

// SLIDER FUNCTIONALITY
let slideIndex = 1;
let slideTimer;

function changeSlide(n) {
  clearTimeout(slideTimer);
  showSlides(slideIndex += n);
  autoSlide();
}

function currentSlide(n) {
  clearTimeout(slideTimer);
  showSlides(slideIndex = n);
  autoSlide();
}

function showSlides(n) {
  const slides = document.querySelectorAll('.slide');
  const dots = document.querySelectorAll('.dot');

  // Eğer slide yoksa çıkış yap (example: galeri sayfasında)
  if (!slides || slides.length === 0) {
    return;
  }

  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }

  slides.forEach(slide => {
    slide.style.display = 'none';
  });

  dots.forEach(dot => {
    dot.classList.remove('active');
  });

  if (slides[slideIndex - 1]) {
    slides[slideIndex - 1].style.display = 'block';
  }
  if (dots[slideIndex - 1]) {
    dots[slideIndex - 1].classList.add('active');
  }
}

function autoSlide() {
  const slides = document.querySelectorAll('.slide');
  if (!slides || slides.length === 0) return;
  
  slideTimer = setTimeout(() => {
    slideIndex++;
    if (slideIndex > slides.length) {
      slideIndex = 1;
    }
    showSlides(slideIndex);
    autoSlide();
  }, 5000); // Change slide every 5 seconds
}

// Initialize slider - only if slides exist
const sliderSlides = document.querySelectorAll('.slide');
if (sliderSlides && sliderSlides.length > 0) {
  showSlides(slideIndex);
  autoSlide();
}

// GALLERY FILTER FUNCTIONALITY - Moved to lazy-loading.js for better performance
// The optimized filter with debouncing and requestAnimationFrame is now in lazy-loading.js


