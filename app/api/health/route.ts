import { NextResponse } from 'next/server'

export async function GET() {
  return NextResponse.json({
    status: 'ok',
    service: 'apex-365-web',
    version: '0.1.0',
    timestamp: new Date().toISOString(),
    capabilities: {
      workspaceShell: true,
      atelierWorkflow: true,
      gabbySurface: true,
      operatorManual: true,
      failSafeRepair: true,
      persistence: false,
      authentication: false,
      integrations: 'not configured',
    },
  })
}
