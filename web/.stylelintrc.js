module.exports = {
    extends: [
      'stylelint-config-standard',
    ],
    plugins: [
      'stylelint-order',
    ],
    ignoreFiles: [
      '**/node_modules/**',
    ],
    rules: {
      'string-quotes': 'single',
    },
  };
