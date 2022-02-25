// ------------ Form submittion / Markdown --------------

// POST to make markdown output
$("#form_project").submit(function (e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);

    $.ajax({
        type: "POST",
        url: "/project",
        data: form.serialize(), // serializes the form's elements.
        success: function (data) {
            window.scrollTo(0, 0);
            document.getElementById("form_div").style = "display: none;";
            document.getElementById("preview").style = "display: block;";
            document.getElementById("markdown-input").value = data;
        }
    });
});

// ------------ Features --------------

// Add feature input
let cont_features = 1;

function addFeatureInput() {
    cont_features++;

    let new_div = document.createElement('div')
    new_div.setAttribute("id", `div_feature${cont_features}`)
    new_div.setAttribute("class", "mt-2")

    new_div.innerHTML = `<input name="features-check" class="form-check-input" type="checkbox" value="feature${cont_features}">`
    new_div.innerHTML += `<label class="form-check-label"> <input name="feature${cont_features}" type="text" class="form-control py-0 px-1"> </label>`
    new_div.innerHTML += `<button type="button" class="btn btn-outline-danger btn-sm py-0 px-1 ms-2 mt-1 mb-2" onclick="removeFeatureInput(div_feature${cont_features})">Remove</button>`

    document.getElementById("features").appendChild(new_div);
}

function removeFeatureInput(div_id) {
    div_id.remove()
}


// ------------ Badges --------------

// Change badges with project insert
let listBadges = [
    "license",
    "repo-size",
    "last-commit",
    "languages/count",
    "contributors",
    "issues-raw",
    "issues-closed-raw",
    "issues-pr-raw",
    "issues-pr-closed-raw"
]

function changeBadges() {
    let githubUsername = document.getElementById("github_username").value;
    let repository = document.getElementById("github_repository").value;

    listBadges.forEach(function (badge) {
        let imageUrl = `https://img.shields.io/github/${badge}/${githubUsername}/${repository}?color=green`;

        document.getElementById(`${badge}-img`).src = imageUrl;
    })
}


// ------------ Contact --------------

//  Put gh_username on "Contact" field with input from "Badges" field

function inputGithubUsername() {
    let github_username = document.getElementById("github_username").value;
    document.getElementById("github_username_contact").value = github_username;
}