export interface ProjectStatus {
  name: string
  stage: string
  message: string
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export async function fetchProjectStatus(): Promise<ProjectStatus> {
  const response = await fetch(`${API_BASE_URL}/api/v1/status`)

  if (!response.ok) {
    throw new Error(`Failed to fetch project status: ${response.status}`)
  }

  return response.json() as Promise<ProjectStatus>
}
