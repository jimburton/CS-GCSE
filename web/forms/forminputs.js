/* Javascript for the form inputs demo. */
// Update range value label
const range = document.getElementById('range');
const rangeVal = document.getElementById('rangeVal');
range.addEventListener('input', () => {
    rangeVal.innerText = range.value;
});

const masterForm = document.getElementById('masterForm');

// Helper to extract form data
function getCleanData() {
    const formData = new FormData(masterForm);
    const data = {};
    formData.forEach((value, key) => {
        if (data[key]) {
            if (!Array.isArray(data[key])) {
                data[key] = [data[key]];
            }
            data[key].push(value);
        } else {
            // For file inputs, just show filename
            if (value instanceof File) {
                data[key] = value.name || "No file selected";
            } else {
                data[key] = value;
            }
        }
    });
    return data;
}

masterForm.onsubmit = (e) => {
    e.preventDefault();
    showDataInModal(getCleanData());
};

function showLivePreview() {
    showDataInModal(getCleanData());
}

function showDataInModal(data) {
    const content = document.getElementById('previewContent');
    content.textContent = JSON.stringify(data, null, 4);
    document.getElementById('previewBox').style.display = 'flex';
}

function closePreview() {
    document.getElementById('previewBox').style.display = 'none';
}

window.onclick = function(event) {
    const modal = document.getElementById('previewBox');
    if (event.target == modal) closePreview();
};

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closePreview();
});
