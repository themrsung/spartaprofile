$(document).ready(function () {
    show_comment();
    
})

function save_comment() {
    let name = $('#user-name').val()
    let comment = $('#user-comment').val()

    $.ajax({
        type: 'POST',
        url: '/mjsungpostcomment',
        data: {
            name_give: name,
            comment_give: comment
        },
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    })
}

function show_comment() {
    $('#profile-comments').empty()
    
    $.ajax({
        type: "GET",
        url: "/mjsunggetcomment",
        data: {},
        success: function (response) {
            let comments = response['comments']
            for (let i = 0; i < comments.length; i++) {
                let name = comments[i]['name']
                let comment = comments[i]['comment']

                let html_temp = `
                <div class="comment">
                    <blockquote class="blockquote mb-0">
                    <p>${comment}</p>
                    <footer class="blockquote-footer">${name}</footer>
                    </blockquote>
                </div>
                 `

                $('#profile-comments').append(html_temp)
            }
        }
    });
}