function openTab(tabName) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.style.display = 'none');
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(btn => btn.classList.remove('active'));
    document.getElementById(tabName).style.display = 'block';
    event.target.classList.add('active');
}

let pyodide = null;

async function initPyodide() {
    pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
    });
}

initPyodide();

async function runCode() {
    if (!pyodide) {
        document.getElementById('output').textContent = 'Pyodide is loading...';
        return;
    }
    const code = document.getElementById('code-input').value;
    try {
        pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
        `);
        const result = await pyodide.runPythonAsync(code);
        const output = pyodide.runPython('sys.stdout.getvalue()');
        pyodide.runPython('sys.stdout = sys.__stdout__');
        document.getElementById('output').textContent = output + (result ? '\n' + result : '');
    } catch (error) {
        document.getElementById('output').textContent = 'Error: ' + error.message;
    }
}