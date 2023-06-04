module.exports = {
  extends: [
    'airbnb',
    'next/core-web-vitals',
    'plugin:import/errors',
    'plugin:import/warnings',
    'plugin:import/typescript',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:storybook/recommended',
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
  plugins: ['@typescript-eslint', 'prefer-arrow'],
  root: true,
  rules: {
    'no-use-before-define': 'off',
    '@typescript-eslint/no-use-before-define': ['error'],
    '@typescript-eslint/no-unused-vars': [
      'error',
      {
        vars: 'all',
        args: 'after-used',
        argsIgnorePattern: '',
        ignoreRestSiblings: false,
        varsIgnorePattern: '',
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
    'react/react-in-jsx-scope': 'off',
    'react/jsx-props-no-spreading': ['off'],
    'react/function-component-definition': [
      2,
      {
        namedComponents: 'arrow-function',
      },
    ],
    'react/prop-types': ['off'], // Moved to overrides
    'import/order': [
      'error',
      {
        groups: [
          'builtin',
          'external',
          'internal',
          ['parent', 'sibling'],
          'object',
          'type',
          'index',
        ],
        'newlines-between': 'always',
        pathGroupsExcludedImportTypes: ['builtin'],
        alphabetize: {
          order: 'asc',
          caseInsensitive: true,
        },
        pathGroups: [
          {
            pattern: '@/libs/',
            group: 'internal',
            position: 'before',
          },
          {
            pattern: '@/generated/',
            group: 'internal',
            position: 'before',
          },
          // ...省略
          {
            pattern: '@/components/ui/',
            group: 'internal',
            position: 'before',
          },
          {
            pattern: './.module.css',
            group: 'index',
            position: 'before',
          },
        ],
      },
    ],
  },
  overrides: [
    {
      files: ['.stories.tsx', 'src/pages/**/'],
      rules: {
        'react/prop-types': 'off',
        'import/no-default-export': 'off',
      },
    },
    {
      files: ['.test.ts', '.mock.ts'],
      rules: {
        'max-lines': 'off',
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
