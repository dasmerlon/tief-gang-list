import eslint from '@eslint/js';
import {configs as tsConfigs, parser as tsParser} from 'typescript-eslint';

export default [
    eslint.configs.recommended,
    ...tsConfigs.recommended,
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
