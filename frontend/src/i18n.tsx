/**
 * Format a date
 */
export function format_date(date: Date): string {
    return new Intl.DateTimeFormat("de-DE").format(date);
}
