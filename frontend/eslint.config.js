import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import tsParser from '@typescript-eslint/parser';

export default [
    eslint.configs.recommended,
    ...tseslint.configs.recommended,
    {
        ignores: [
            "**/*.log",
            "dist",
            "src/api",
            "tailwind.config.js",
            ".parcel-cache",
            "node_modules",
        ],
    },
    {
        files: ["src/**/*.tsx"],
        languageOptions: {
            parser: tsParser,
        },
        rules: {
            "@typescript-eslint/no-non-null-assertion": "off",
            indent: [
                "error",
                4
            ],
        }
    }
];
