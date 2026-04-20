document.addEventListener('DOMContentLoaded', () => {
  // Form
  const form = document.querySelector('#myForm');

  // Buttons
  const getButton = document.querySelector('#getButton');
  const postButton = document.querySelector('#postButton');

  // Containers
  const quantityContainer = document.querySelector('#quantity_container');
  const commentContainer = document.querySelector('#comment_container');

  // Input
  const quantityInput = document.querySelector('#quantity');
  const comment = document.querySelector('#comment');

  function toggleQuantity() {
    if (form.method === 'get') {
      quantityContainer.style.display = 'none';
      quantityInput.disabled = true;
      commentContainer.style.display = 'block';
      comment.disabled = false;
    } else if (form.method === 'post') {
      quantityContainer.style.display = 'block';
      quantityInput.disabled = false;
      commentContainer.style.display = 'none';
      comment.disabled = true;
    } else {
      alert('Unknown method!');
    }
  }

  toggleQuantity();

  getButton.addEventListener('click', () => {
    form.method = 'get';
    toggleQuantity();
  });

  postButton.addEventListener('click', () => {
    form.method = 'post';
    toggleQuantity();
  });
})

