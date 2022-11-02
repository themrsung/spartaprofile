$(document).ready(function () {
    show_comment();
    show_reputation();
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

function log_reputations() {
    ($('#current-reputation')).val(1);
    console.log($('#current-reputation').val());
    console.log($('#user-reputation').val());
}

function save_reputation() {
    rep = $('#user-reputation').val();

    $.ajax({
        type: "POST",
        url: "/mjsungpostrep",
        data: {
            rep_give: rep
        },
        success: function (response) {
            alert(response['msg'])
            show_reputation()
            $('#user-reputation').hide();
            $('#user-reputation-button').hide();
            $('#user-reputation-title').hide();
        }
    });
}

function show_reputation() {
    $.ajax({
        type: "GET",
        url: "/mjsunggetrep",
        data: {},
        success: function (response) {
            let rep = response['avg']

            console.log(rep)

            $('#current-reputation').val(rep);
        }
    });
}

// function test() {
//     $.ajax({
//         type: "GET",
//         url: "/mjsungcommentdeletetest",
//         data: {},
//         success: function (response) {
//             let comments = response['comments']
//             console.log(typeof comments)
//             for (let i = 0; i < comments.length; i++) {
//                 let id = comments[i]['_id']
//                 console.log(typeof id)
//             }
//         }
//     });
// }