// -------------------------------------------------------------------------------------------------
// JavaScript Snow Effect - © Copyright 2020 - Jam-Es.com
// Licensed under the MIT License (MIT). See LICENSE in the repo root for license information.
// -------------------------------------------------------------------------------------------------

var numParticles = window.innerWidth / 3,
    maxSpeed = 0.8,
    minSpeed = 0.4,
    maxSize = 5,
    minSize = 3,
    maxOpacity = 1,
    minOpacity = .2,
    canvasId = "snowcanvas",
    fixCanvasResolution = !0,
    snow_particles = [];

function Redraw() {
    var n = document.getElementById(canvasId),
        e = n.getContext("2d");
    for (e.clearRect(0, 0, n.width, n.height), i = 0; i < snow_particles.length; i++) {
        var t = snow_particles[i].yPos + snow_particles[i].speed;
        t > window.innerHeight && (t = getRandomInt(-100, -10), snow_particles[i].xPos = getRandomInt(0, window.innerWidth), snow_particles[i].speed = Math.random() * (maxSpeed - minSpeed) + minSpeed, snow_particles[i].opacity = Math.random() * (maxOpacity - minOpacity) + minOpacity, snow_particles[i].size = Math.random() * (maxSize - minSize) + minSize), snow_particles[i].yPos = t, e.beginPath(), e.arc(snow_particles[i].xPos, t, snow_particles[i].size, 0, 2 * Math.PI), e.fillStyle = "rgba(255, 255, 255, " + snow_particles[i].opacity + ")", e.fill()
    }
}

function InitPoints() {
    for (i = 0; i < numParticles; i++) {
        var n = getRandomInt(0, window.innerWidth),
            e = getRandomInt(0, window.innerHeight),
            t = Math.random() * (maxSpeed - minSpeed) + minSpeed,
            a = Math.random() * (maxOpacity - minOpacity) + minOpacity,
            o = Math.random() * (maxSize - minSize) + minSize;
        snow_particles.push({
            xPos: n,
            yPos: e,
            speed: t,
            opacity: a,
            size: o
        })
    }
}

function getRandomInt(i, n) {
    return i = Math.ceil(i), n = Math.floor(n), Math.floor(Math.random() * (n - i)) + i
}
window.onload = function() {
    var i;
    fixCanvasResolution && ((i = document.getElementById(canvasId)).width = window.innerWidth, i.height = window.innerHeight), InitPoints(), setInterval(Redraw, 5)
};
