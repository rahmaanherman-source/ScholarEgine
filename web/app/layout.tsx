import { Analytics } from '@vercel/analytics/next';
import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'ScholarEgine',
  description: 'GODSPEED Scholar / Research Engine - Evidence-first research and source-ingestion surface',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
