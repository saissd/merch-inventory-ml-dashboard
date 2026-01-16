const API_BASE = import.meta.env.VITE_API_BASE ?? "http://127.0.0.1:8000";

export async function getSummary() {
  return (await fetch(`${API_BASE}/summary`)).json();
}
export async function getFutureForecast(store_id?: string, item_id?: string) {
  const usp = new URLSearchParams();
  if (store_id) usp.set("store_id", store_id);
  if (item_id) usp.set("item_id", item_id);
  return (await fetch(`${API_BASE}/forecast/future?${usp.toString()}`)).json();
}
export async function getRecs(kind: string, store_id?: string) {
  const usp = new URLSearchParams();
  if (store_id) usp.set("store_id", store_id);
  return (await fetch(`${API_BASE}/recs/${kind}?${usp.toString()}`)).json();
}
export async function runPipeline(endpoint: string, zip_path: string, max_series: number) {
  return (await fetch(`${API_BASE}/pipeline/${endpoint}`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ zip_path, max_series })
  })).json();
}
