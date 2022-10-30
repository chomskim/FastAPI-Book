import { useRouter } from 'next/router'
import { useEffect } from 'react'
import axios from 'axios'
import useAuth from '../../hooks/useAuth'

const Logout = () => {
  const { user, setUser } = useAuth()
  const removeCookie = async () => {
    const res = await axios.post('/api/logout', {}, { headers: { 'Content-Type': 'application/json' } })
    console.log('res=', res)
  }
  const router = useRouter()
  useEffect(() => {
    removeCookie()
    setUser(null)

    router.push('/')
  }, [])

  return <></>
}

export default Logout
