
/* 木構造の全探索のイメージ：幅優先探索が良い */
function func1(e) {
    id = e.getAttribute('class').split(' ')
    /* e.classList.toggle("active") */
    console.log($(`#${id}`).children())
    console.log($(`#${id}`).find())
    $(`#${id}`).children().toggleClass('active')
}

function func2(e) {
    id = e.getAttribute('class')
    $(`#${id}`).children().toggleClass('active')
    console.log(id, $(`#${id}`))
}
