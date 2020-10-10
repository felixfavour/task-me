const csrftoken = Cookies.get('csrftoken')
let deleteButton = document.querySelectorAll('.delete-btn')
let ipButton = document.querySelectorAll('.ip-btn')
let doButton = document.querySelectorAll('.do-btn')

let deleteTask = async (url) => {
    newUrl = window.location.href + url
    const response = await fetch(newUrl, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    });
    const responseData = await window.location.reload();
    return responseData;
}

//for
//deleteButton.forEach(button => {
//    const =
//    addEventListener('click', () => {
//        url = window.location.href + button.value
//        deleteTask(url)
//    })
//})

let updateTask = async (url, name, status) => {
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            "name": name,
            "status": status
        })
    });
    const responseData = await window.location.reload()
    return responseData
}
