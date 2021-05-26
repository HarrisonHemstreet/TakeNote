const deleteNote = noteId => {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

const editNote = noteId => {
    fetch("/edit-note", {
        method: "GET",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}