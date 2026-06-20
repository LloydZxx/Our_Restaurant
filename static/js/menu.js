new Swiper('.card-wrapper', {
  loop: true,
  spaceBetween: 30,

  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    dynamicBullets: true,
  },

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  breakpoints: {
    0: {
        slidesPerView: 1.2,   
        spaceBetween: 15, 
    },

    768: {
        slidesPerView: 2,
        spaceBetween: 30,
    },
  
    1024: {
        slidesPerView: 3,
        spaceBetween: 30,
    },
  },
});