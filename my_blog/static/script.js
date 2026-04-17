const authorNameEmail = document.querySelector('#author-name-email');
const authorYes = document.querySelector('#author-yes');

const allDataButton = document.querySelector('#all-data');
const yesNamesButton = document.querySelector('#yes-names');

allDataButton.addEventListener('click', () => {
  authorNameEmail.style.display = 'block';
  authorYes.style.display = 'none';
})

yesNamesButton.addEventListener('click', () => {
  authorNameEmail.style.display = 'none';
  authorYes.style.display = 'block';
})