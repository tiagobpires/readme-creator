// Save data traffic information
if (!(sessionStorage.getItem("profile_readme"))) {
    sessionStorage.setItem("profile_readme", "false");
}
if (!(sessionStorage.getItem("project_readme"))) {
    sessionStorage.setItem("project_readme", "false");
}

if (!(sessionStorage.getItem("visit"))) {
    sessionStorage.setItem("visit", "true");
    $.ajax({
        type: "GET",
        url: "/analytics/visits",
    });
}


// Search Skills
function search_skill() {
    let input = document.getElementById('searchbar_skills').value;
    input = input.toLowerCase();
    let names = document.getElementsByClassName('skill_name');
    let div = document.getElementsByClassName('skill_div');

    for (i = 0; i < names.length; i++) {
        if (!names[i].value.toLowerCase().includes(input)) {
            div[i].style.display = "none";
        }
        else {
            div[i].style.display = "block";
        }
    }
}

// ------------ NavBar Markdown --------------

// Transform preview data (markdown) in html 
$("#preview-tab").click(function () {
    markdown = document.getElementById("markdown-input").value;
    $.ajax({
        type: "POST",
        url: "/preview",
        data: { 'data': markdown },
        success: function (data) {
            document.getElementById("preview-content").innerHTML = data;
        }
    });
});

// Set display of the form
$("#back_to_form").click(function () {
    document.getElementById("form_div").style = "display: block;";
    document.getElementById("preview").style = "display: none;";
    window.scrollTo(0, 0);
});

// Copy readme
$("#copy_readme").click(function () {
    readme = document.getElementById("markdown-input").value;
    button = document.getElementById("copy_readme");

    navigator.clipboard.writeText(readme).then(function () {
        button.innerHTML = 'Copied!';
        setTimeout(function () {
            button.innerHTML = 'Copy to Clipboard'
        }, 3000);
    }, function (err) {
        button.innerHTML = 'Sorry, something went wrong';
        setTimeout(function () {
            button.innerHTML = 'Copy to Clipboard'
        }, 3000);
    });
})