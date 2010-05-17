$(window).load(function() {
    var links = $('#nav');
    var photo = $('#photo img');
    if (links.length == 0) { return; }
    if (photo.length != 1) { return; }
    
    var next = $('li.next a', links).get(0);
    var prev = $('li.previous a', links).get(0);
    var parent = photo.parent().addClass('photo-nav');
    var menu = $('<div class="photo-nav-menu"></div>');
    
    parent.append(menu);
    
    var offset_top = (parent.height() - photo.height()) / 2;
    var offset_left = (parent.width() - photo.width()) / 2;
    menu.css({
        top: offset_top + 'px',
        left: offset_left + 'px'
    });
    menu.height(photo.height()).width(photo.width());
    
    var add_link = function(img, rel, link) {
        if (rel == undefined || link == undefined) { return ;}
        link = $(link);
        
        l = $(document.createElement('a')).attr('href', link.attr('href')).addClass(rel);
        l.html('&nbsp;').appendTo(menu);
        l.height(menu.height());
    };
    
    add_link(photo, 'next', next);
    add_link(photo, 'prev', prev);
});