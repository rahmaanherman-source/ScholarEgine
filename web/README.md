# ScholarEgine Web Interface

This is the web frontend for ScholarEgine - GODSPEED Scholar / Research Engine.

## Features

- ✅ Vercel Web Analytics configured
- Built with Next.js 16 (App Router)
- TypeScript support
- Static export for optimal performance

## Getting Started

### Development

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to see the application.

### Build

```bash
npm run build
```

This creates an optimized production build in the `out` directory.

### Deploy to Vercel

This project is ready to deploy to Vercel:

1. Push the code to your repository
2. Import the project on [Vercel](https://vercel.com/new)
3. Vercel will automatically detect the Next.js configuration
4. Enable Web Analytics in your Vercel project dashboard
5. Deploy!

The `<Analytics />` component from `@vercel/analytics` is already integrated in `app/layout.tsx`.

## Project Structure

```
web/
├── app/
│   ├── layout.tsx       # Root layout with Analytics component
│   ├── page.tsx         # Home page
│   └── globals.css      # Global styles
├── package.json         # Dependencies and scripts
├── next.config.js       # Next.js configuration
└── tsconfig.json        # TypeScript configuration
```

## Analytics

Vercel Web Analytics is configured and will automatically track:
- Page views
- Navigation events
- Performance metrics

To view analytics data, go to your project dashboard on Vercel and navigate to the Analytics tab.
