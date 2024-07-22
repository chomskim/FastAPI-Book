import axios from 'axios'

export default async function (req, res) {
  if (req.method === 'GET') {
    const { jwt } = req.cookies

    if (!jwt) {
      res.status(401).end()
      return
    }

    try {
      const headers = {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${jwt}`,
      }
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/users/me`, { headers })
      console.log('response=', response)
      const userData = response.data
      userData['jwt'] = jwt
      res.status(200).json(userData).end()
    } catch (error) {
      res.status(401).end()
      return
    }
  } else {
    res.setHeader('Allow', ['GET'])
    res
      .status(405)
      .json({ message: `Method ${req.method} not allowed` })
      .end()
  }
}
