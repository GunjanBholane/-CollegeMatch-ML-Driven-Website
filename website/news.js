// Function to show the modal
function showModal(src) {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("fullImage");

    modal.style.display = "block";
    modalImg.src = src;
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById("imageModal");
    modal.style.display = "none";
}
