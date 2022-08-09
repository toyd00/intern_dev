function func1(e) {
    id = e.getAttribute('class').split(' ')
    /* e.classList.toggle("active") */
    console.log(id[0])
    $(`#${id}`).children().toggleClass('active')
}

function func2(e) {
    id = e.getAttribute('class')
    $(`#${id}`).children().toggleClass('active')
    console.log(id, $(`#${id}`))
}
