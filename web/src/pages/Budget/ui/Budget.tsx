import { useParams } from "@solidjs/router"

export default () => {
  const params = useParams()
  return (
    <div>
      {params.budgetId}
    </div>
  )
}