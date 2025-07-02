const name = document.querySelector('h1').textContent.split(' ')[2]
fetch(`http://localhost:8000/display_stud_detail/?name=${name}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parse JSON data
    })
    .then(data => {
        console.log('JSON Data:', data); // Use the data as needed
        // Example: Display the message in the console
        document.getElementById('output').outerHTML = `<div id="output">
                                                                    <b>Name</b>: ${data.name}</br>
                                                                    <b>Gender</b>: ${data.gender}</br>
                                                                    <b>DoB</b>: ${data.dob}</br>
                                                                    <b>Email</b>: ${data.email}</br>
                                                                    <b>Phone</b>: ${data.phone}</br></div>
                                                                </div>`;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });

function theme_change() {
    const toggleButton = document.getElementById('theme-toggle');
    toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        if (document.body.classList.contains('dark-theme')) {
            toggleButton.textContent = 'Light Theme';
        } else {
            toggleButton.textContent = 'Dark Theme';
        }
    });
}