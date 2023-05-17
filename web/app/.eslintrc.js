module.exports = {
    extends: [
      'next/core-web-vitals',
      'plugin:import/errors',
      'plugin:import/warnings',
      'plugin:import/typescript',
      'plugin:@typescript-eslint/recommended',
      'plugin:@typescript-eslint/recommended-requiring-type-checking',
      'prettier',
    ],
    parserOptions: {
      ecmaFeatures: {
        jsx: true,
      },
      ecmaVersion: 'latest',
      project: './tsconfig.eslint.json',
      sourceType: 'module',
    },
    plugins: [
      '@typescript-eslint',
      'prefer-arrow',
    ],
    root: true,
    rules: {
      'no-use-before-define': 'off',
      '@typescript-eslint/no-use-before-define': ['error'],
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          vars: 'all',
          args: 'after-used',
          argsIgnorePattern: '_',
          ignoreRestSiblings: false,
          varsIgnorePattern: '_',
        },
      ],
      'import/extensions': [
        'error',
        'ignorePackages',
        {
          js: 'never',
          jsx: 'never',
          ts: 'never',
          tsx: 'never',
        },
      ],
      'react/jsx-filename-extension': [
        'error',
        {
          extensions: ['.jsx', '.tsx'],
        },
      ],
      'react/jsx-props-no-spreading': [
        'error',
        {
          html: 'enforce',
          custom: 'enforce',
          explicitSpread: 'ignore',
        },
      ],
      'react/react-in-jsx-scope': 'off',
      'react/jsx-props-no-spreading': ['off'],
      'react/function-component-definition': [
        2,
        {
          namedComponents: 'arrow-function',
        },
      ],
    },
    overrides: [
      {
        files: ['*.tsx'],
        rules: {
          'react/prop-types': 'off',
        },
      },
    ],
    settings: {
      'import/resolver': {
        node: {
          paths: ['src'],
        },
      },
    },
};
