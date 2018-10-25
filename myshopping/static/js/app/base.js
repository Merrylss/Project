$(function() {
    $('.type1li').mouseover(function () {
        $(this).children('ul').css('display', 'block')
    });
    $('.type1li').mouseout(function () {
        $(this).children('ul').css('display', 'none')
    });
});

