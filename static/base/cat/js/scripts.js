/*!
* Start Bootstrap - Blog Home v5.0.2 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(".like-area a").click(function() {
    if ($(this).hasClass("like-active")) {
     $(this).find('.like-no').html(parseInt($(this).find('.like-no').html(), 10) - 1)
    } else {
     $(this).find('.like-no').html(parseInt($(this).find('.like-no').html(), 10) + 1)
    }
    $(this).toggleClass('like-active');
   });