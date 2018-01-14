$(function () {
  count = 0;
  wordsArray = ["Developer", "Pythonista", "Gamer", "Cat lover"];
  setInterval(function () {
    count++;
    $(".word").fadeOut(400, function () {
      $(this).text(wordsArray[count % wordsArray.length]).fadeIn(400);
    });
  }, 4000);
});