document.getElementById('csvForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const file1 = document.getElementById('file1').files[0];
    const file2 = document.getElementById('file2').files[0];

    if (file1 && file2) {
        console.log('File 1:', file1);
        console.log('File 2:', file2);
        alert('Files uploaded successfully!');
    } else {
        alert('Please select both CSV files.');
    }
});
