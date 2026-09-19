/* Cutelemon6 preview adapter. CodeMirror is used only by this browser preview. */
(() => {
  const modes = {
    python: 'python', py: 'python', bash: 'shell', sh: 'shell', shell: 'shell',
    javascript: 'javascript', js: 'javascript', json: { name: 'javascript', json: true }
  };
  document.querySelectorAll('pre > code[class*="language-"]').forEach(code => {
    const language = [...code.classList].find(name => name.startsWith('language-'))?.slice(9);
    const mode = modes[language];
    if (!mode) return;
    const source = code.textContent;
    CodeMirror.runMode(source, mode, code, { tabSize: 4 });
    code.parentElement.classList.add('cm-s-inner');
  });
})();
