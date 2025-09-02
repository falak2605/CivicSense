// CSRF helper
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const csrftoken = getCookie('csrftoken');

async function fetchIssues() {
  const res = await fetch('/api/issues/');
  const data = await res.json();
  const list = document.getElementById('issuesList');
  list.innerHTML = '';
  data.forEach(it => {
    const li = document.createElement('li');
    li.className = 'issue';
    li.innerHTML = `
      <h3>${it.title}</h3>
      <div><span class="badge">${it.category}</span>
           <span class="badge status-${it.status.replace(' ','-')}">${it.status}</span>
      </div>
      <div class="meta">${new Date(it.created_at).toLocaleString()} • Upvotes: ${it.upvotes}</div>
      <p>${it.description}</p>
      <div class="actions">
        <button data-id="${it.id}" class="upvoteBtn">Upvote</button>
        <button data-id="${it.id}" class="markProgressBtn">Mark In Progress</button>
        <button data-id="${it.id}" class="markResolvedBtn">Mark Resolved</button>
      </div>
    `;
    list.appendChild(li);
  });

  // attach handlers
  document.querySelectorAll('.upvoteBtn').forEach(btn => {
    btn.onclick = async () => {
      const id = btn.getAttribute('data-id');
      await fetch(`/api/issues/${id}/upvote/`, { method: 'POST', headers: { 'X-CSRFToken': csrftoken } });
      fetchIssues();
    };
  });
  document.querySelectorAll('.markProgressBtn').forEach(btn => {
    btn.onclick = async () => {
      const id = btn.getAttribute('data-id');
      await fetch(`/api/issues/${id}/status/`, { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken }, body: JSON.stringify({ status: 'In Progress' }) });
      fetchIssues();
    };
  });
  document.querySelectorAll('.markResolvedBtn').forEach(btn => {
    btn.onclick = async () => {
      const id = btn.getAttribute('data-id');
      await fetch(`/api/issues/${id}/status/`, { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken }, body: JSON.stringify({ status: 'Resolved' }) });
      fetchIssues();
    };
  });
}

document.getElementById('locateBtn').addEventListener('click', () => {
  if (!navigator.geolocation) return alert('Geolocation not supported');
  navigator.geolocation.getCurrentPosition(pos => {
    document.getElementById('lat').value = pos.coords.latitude.toFixed(6);
    document.getElementById('lng').value = pos.coords.longitude.toFixed(6);
  }, err => alert('Could not get location'));
});

document.getElementById('issueForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    title: document.getElementById('title').value.trim(),
    description: document.getElementById('description').value.trim(),
    category: document.getElementById('category').value,
    location_lat: document.getElementById('lat').value ? parseFloat(document.getElementById('lat').value) : null,
    location_lng: document.getElementById('lng').value ? parseFloat(document.getElementById('lng').value) : null
  };
  if (!payload.title || !payload.description) {
    alert('Please fill title and description'); return;
  }
  await fetch('/api/issues/create/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
    body: JSON.stringify(payload)
  });
  // reset form & reload
  e.target.reset();
  fetchIssues();
});

// initial load
fetchIssues();
