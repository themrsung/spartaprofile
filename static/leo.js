$(document).ready(function () {
    show_comment()
})

function useState(initialValue) {
    let value = initialValue
    const state = () => value

    function setState(newValue) {
        value = newValue || state()
    }

    return [state, setState]
}

let id = null

function save_comment() {
    const uuid = Math.floor(Math.random() * 10000000)
    const name = $("#name").val()
    const comment = $("#comment").val()

    $.ajax({
        type: "POST",
        url: "/comment",
        data: { uuid_give: uuid, name_give: name, comment_give: comment },
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        },
    })
}

function handleClickEdit(e, uuid) {
    id = e.target.parentElement.parentElement.id

    if (id == uuid) {
        const temp_html = `<input type="text" class="form-control" id="editComment" />
                            <input type="text" class="form-control" id="editName" />
                            <button type="button" onclick="update_comment(event)" class="btn btn-outline-primary">완료</button>`

        $("#" + id).append(temp_html)
    } else {
        throw Error()
    }
}

function update_comment(e) {
    const uuid = e.target.parentElement.id
    const name = $("#editName").val()
    const comment = $("#editComment").val()

    $.ajax({
        type: "PATCH",
        url: "/comment",
        data: { uuid_give: uuid, name_give: name, comment_give: comment },
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        },
    })
}

function delete_comment(uuid) {
    $.ajax({
        type: "DELETE",
        url: "/comment",
        data: { uuid_give: uuid },
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        },
    })
}

function show_comment() {
    $.ajax({
        type: "GET",
        url: "/comment",
        data: {},
        success: function (response) {
            const rows = response["post"]
            rows.forEach((item) => {
                const uuid = item.uuid
                const name = item.name
                const comment = item.comment

                const temp_html = `<div id="card" class="card">
                                        <div id=${uuid} class="card-body">
                                            <blockquote class="blockquote mb-0">
                                                <p>${comment}</p>
                                                <footer class="blockquote-footer">${name}</footer>
                                            </blockquote>
                                            <div class="card-button">
                                            <button type="button" onclick="handleClickEdit(event, ${uuid})" class="btn btn-outline-primary">수정</button>
                                            <button type="button" onclick="delete_comment(${uuid})" class="btn btn-outline-primary">삭제</button>
                                            </div>
                                        </div>
                                    </div>`
                $("#commentList").append(temp_html)
            })
        },
    })
}
