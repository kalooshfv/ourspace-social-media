
let filtered = false;
let creatingPost = false;

$(document).ready(function() {
    refresh();
})

async function get_posts() {
if (filtered == true) {
    return fetch("/api/posts/{{user.pk}}").then((res) => res.json())
} else {
    return fetch("{% url 'backend:posts' %}").then((res) => res.json())
}};

async function refresh() {
document.getElementById("displayWindow").innerHTML = "";
const posts = await get_posts();
    let html_string = "";
    posts.data.forEach((post) => {
    if (post.creator_username == "{{user.username}}") {
        footer =
        `
        <div class="row">
        <div class="col mx-auto"><button onclick="editMode(${post.id})" class="btn btn-outline-light btn-block w-100"style="background-color: rgba(255,0,255, 0.5);"">Edit this post!</button></div>
        <div class="col mx-auto"><button onclick="deletePost(${post.id})" class="btn btn-outline-light btn-block w-100"style="background-color: rgba(255,0,255, 0.5);"">Delete this post!</button></div>
        </div>
        `
    } else {
        footer =
        `
        
        `
    }
    html_string +=
    `
    <div id="post-${post.id}" class="row rounded mx-auto my-2" 
        style="padding-bottom: 1em; padding-top: 1em; background-color: rgba(255,0,255, 0.5); outline: pink;">
        <div class="col-3">
        <img src="/media/${post.creator_image}" style='object-fit: cover'/>
        </div>
        <div class="col mx-auto justify-content-center">
        <div class="card w-100" style="opacity: 0.8">
            <div class="card-body h-100">
            <h5 class="card-title">${post.creator_username} said...</h5>
            <h6 class="card-subtitle mb-2 text-muted">On ${post.date}...</h6>
            <p id="post-${post.id}-content" class="card-text">
            ${post.content}
            </p>
            </div>
            <div id="post-${post.id}-footer" class="card-footer text-muted">
            ${footer}
            </div>
        </div>
        </div>
    </div>
    `
    });
    document.getElementById("displayWindow").innerHTML = html_string;
};


async function editMode(id) {
document.getElementById("post-" + id + "-content").innerHTML =
`
<textarea class="form-control rounded" 
    id="post-${id}-fill" style="background-color: rgba(255,0,255, 0.5); color: white;">
</textarea>
`
document.getElementById("post-" + id + "-footer").innerHTML =
`
<div class="col mx-auto"><button onclick="editPost(${id})" class="btn btn-outline-light btn-block w-100"style="background-color: rgba(255,0,255, 0.5);"">Finish editing!</button></div>
`
}

async function editPost(id) {
event.preventDefault()

const new_content = $("#post-" + id + "-fill").val();
const csrftoken = $("[name=csrfmiddlewaretoken]").val();
console.log(new_content)

$.ajax({
    url: "{% url 'backend:posts' %}" + id,
    method: 'PATCH',
    headers: {
    'X-CSRFToken': csrftoken
    },
    data: {
    content: new_content,
    },
    success: function(response) {
    console.log(response);
    $('#PostContent').val('');
    refresh();
    },
    error: function(xhr, errmsg, err) {
    console.log(xhr.status + ": " + xhr.responseText);
    }
})
refresh();
}



async function createPost() {
event.preventDefault();

if (creatingPost) {
    return; 
}

const content = $('#post-content').val();
const csrftoken = $("[name=csrfmiddlewaretoken]").val();

creatingPost = true; 

try {
    const response = await $.ajax({
    url: "{% url 'backend:posts' %}",
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken
    },
    data: {
        content: content,
    },
    });

    console.log(response);
    $('#post-content').val('');
    refresh();
} catch (error) {
    console.log(error.status + ": " + error.responseText);
} finally {
    creatingPost = false;
}
};

async function filterPost() {
filtered = !filtered
console.log(filtered)
if (filtered == true) {
    refresh();
    document.getElementById("filter-post").innerHTML = "MY <br> POSTS";
} else if (filtered == false) {
    refresh();
    document.getElementById("filter-post").innerHTML = "ALL <br> POSTS";
}
};

async function deletePost(id) {
const csrftoken = $("[name=csrfmiddlewaretoken]").val();

try {
    const response = await $.ajax({
        url: "{% url 'backend:posts' %}" + id,
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrftoken
        }
    });
    refresh();
} catch (error) {
    console.log(error);
}
}