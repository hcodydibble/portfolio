$('.contact-view').hover(function(){
    $(".fa-address-book-o").fadeTo("slow", 0)
    $('.fade').fadeTo("slow", 1)
}, function(){
    $(".fade").fadeTo("slow", 0)
    $(".fa-address-book-o").fadeTo("slow", 1)
})

// var timer;
// $('.contact-view').on("mouseenter", ".fa-address-book-o", function(){
//     $('.fa-address-book-o').fadeOut("slow")
//     timer = setTimeout(function(){
//         $('.contact-view p').css("visibility", "visible")
//     }, 2000)
// })