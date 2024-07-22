import Link from 'next/link'
import axios from 'axios'
import useAuth from '../hooks/useAuth'
import { useEffect } from 'react'

const Header = () => {
  const { user, setUser, loading, setLoading } = useAuth()
  console.log('user=', user)
  useEffect(() => {
    const getUser = async () => {
      try {
        const response = await axios.get('/api/user')
        console.log('response=', response)
        const user = response.data
        setUser(user)
      } catch (error) {
        console.log(error)
        setUser(null)
      }
      getUser()
    }
  }, [])
  return (
    <div className=' text-orange-600 py-2 font-bold flex flex-row justify-between items-center'>
      <div>
        {loading ? <span>Loading...</span> : ''}
        <Link href='/'>
          FARM Cars
          {user ? (
            <span className='mx-2 text-gray-500'>
              {user.username} ({user.role})
            </span>
          ) : (
            ''
          )}
        </Link>
      </div>
      <ul className='flex flex-row space-x-4 '>
        <li>
          <Link href='/cars'>Cars</Link>
        </li>
        {user && user.role === 'ADMIN' ? (
          <li>
            <Link href='/cars/add'>Add Car</Link>
          </li>
        ) : (
          ''
        )}

        {!user ? (
          <>
            <li>
              <Link href='/account/register'>Register</Link>
            </li>
            <li>
              <Link href='/account/login'>Login</Link>
            </li>
          </>
        ) : (
          <>
            <li>
              <Link href='/account/logout'>Log out {user.username}</Link>
            </li>
          </>
        )}
      </ul>
    </div>
  )
}
export default Header
