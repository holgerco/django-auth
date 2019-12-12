const title = document.querySelector('.error_title');

//////// Light //////////
document.onmousemove = function (e) {
    let x = e.pageX - window.innerWidth / 2;
    let y = e.pageY - window.innerHeight / 2;

    title.style.setProperty('--x', x + 'px');
    title.style.setProperty('--y', y + 'px')
};

////////////// Shadow ///////////////////
title.onmousemove = function (e) {
    let x = e.pageX - window.innerWidth / 2;
    let y = e.pageY - window.innerHeight / 2;

    let rad = Math.atan2(y, x).toFixed(2);
    let length = Math.round(Math.sqrt((Math.pow(x, 2)) + (Math.pow(y, 2))) / 10);

    let x_shadow = Math.round(length * Math.cos(rad));
    let y_shadow = Math.round(length * Math.sin(rad));

    title.style.setProperty('--x-shadow', -x_shadow + 'px');
    title.style.setProperty('--y-shadow', -y_shadow + 'px');

};