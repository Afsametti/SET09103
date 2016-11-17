// menu smothness
// version 1.0.2

$(function(){

  // dropdown menu with 3 levels

  //$('.menusm li').click(function() {
  //  window.location = $(this).find('a:first').attr('href');
  //});
  var level=0;
  $('.sf-menu').find('li:first-child').addClass('ms_first');
  $('.sf-menu').find('li:last-child').addClass('ms_last');
  $('.sf-menu').find('li:first-child').children('a').addClass('ms_first');
  $('.sf-menu').find('li:last-child').children('a').addClass('ms_last');
  $('.sf-menu ul').find('li:first-child').addClass('ms_first');
  $('.sf-menu ul').find('li:last-child').addClass('ms_last');
  $('.sf-menu ul').find('li:first-child').children('a').addClass('ms_first');
  $('.sf-menu ul').find('li:last-child').children('a').addClass('ms_last');
  $('.sf-menu').children('li').addClass('ms_top');
  $('.sf-menu').children('li').children('a').addClass('ms_top');
  $('.sf-menu').children('li').children('ul').parent().addClass('ms_havesubmenu');
  $('.sf-menu').children('li').children('ul').parent().children('a').addClass('ms_havesubmenu');
  $('.sf-menu ul li').children('ul').parent().addClass('ms_havesubmenu');
  $('.sf-menu ul li').children('ul').parent().children('a').addClass('ms_havesubmenu');
  $('.sf-menu li').hover(function(){
    $(this).find('ul:first').stop(true,true).slideDown(300).show();
    $(this).addClass('ms_hover');
    $(this).children('a').addClass('ms_hover');
    level++;
  },function(){
    $(this).find('ul:first').stop(true,true).slideUp(200);
    $(this).removeClass('ms_hover');
    $(this).children('a').removeClass('ms_hover');
    level--;
  });

  // tab-navigation

  $('#mstabs').find('ul:first').find('li:first').children('a').addClass('ms_active');
  $('#mstabs').children('div').css({'display':'none'});
  $('#'+$('#mstabs').find('a.ms_active:first').attr('rel')).css({'display':'block'});
  $('#mstabs').find('ul:first').children('li').children('a').click(function() {
	$('#mstabs').find('ul:first').children('li').children('a').removeClass('ms_active');
	$(this).addClass('ms_active');
	$('#mstabs').children('div').css({'display':'none'});
	$('#'+$(this).attr('rel')).css({'display':'block'});
	return false;
  });

});

