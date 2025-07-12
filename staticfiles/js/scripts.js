document.addEventListener('DOMContentLoaded', function () {
  const form1 = document.getElementById('filter-form-1');
  const form2 = document.getElementById('filter-form-2');
  const resultsContainer = document.getElementById('results-container');

  // Collect data from both forms and merge with extra data (e.g. page)
  function collectFormData(extra = {}) {
    const combinedData = new FormData();

    if (form1) {
      new FormData(form1).forEach((value, key) => {
        combinedData.append(key, value);
      });
    }

    if (form2) {
      new FormData(form2).forEach((value, key) => {
        combinedData.append(key, value);
      });
    }

    for (const key in extra) {
      combinedData.append(key, extra[key]);
    }

    return combinedData;
  }

  // Fetch and update results via AJAX
  function updateResults(extra = {}) {
    const formData = collectFormData(extra);

    fetch('/jobslist/', {
      method: 'POST',
      body: formData,
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    .then(response => response.text())
    .then(data => {
      resultsContainer.innerHTML = data;
      attachPaginationHandlers();  // Reattach after content updates
    });
  }

  // Re-attach AJAX handlers to pagination links
  function attachPaginationHandlers() {
    const pageLinks = resultsContainer.querySelectorAll('.pagination a');

    pageLinks.forEach(link => {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        const url = new URL(this.href, window.location.origin);
        const page = url.searchParams.get('page');
        updateResults({ page: page });
      });
    });
  }

  // Add listeners for filtering forms
  [form1, form2].forEach(form => {
    if (form) {
      form.addEventListener('input', () => updateResults());
      form.addEventListener('change', () => updateResults());
    }
  });

  // Initial load: fetch results immediately
  updateResults(); // ✅ This line ensures results load immediately on page load
});
