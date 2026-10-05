import { Container, FormTitle, Main, Form, Button, FileInput } from '../../components'
import styles from './styles.module.css'
import { useHistory } from 'react-router-dom'
import { useContext, useState } from 'react'
import { AuthContext, UserContext } from '../../contexts'
import MetaTags from 'react-meta-tags'

const UpdateAvatar = ({
  onAvatarChange
}) => {
  const userContext = useContext(UserContext)
  
  const [ avatarFile, setAvatarFile ] = useState(userContext.avatar || null)
  const [ updated, setUpdated ] = useState(false)

  const checkIfDisabled = () => {
    return avatarFile === '' ||
    avatarFile === null || 
    !updated
  }

  return <Main withBG asFlex>
    <Container className={styles.center}>
      <MetaTags>
        <title>Sign up</title>
        <meta name="description" content="Foodgram - Edit avatar" />
        <meta property="og:title" content="Edit avatar" />
      </MetaTags>
      <Form
        className={styles.form}
        onSubmit={e => {
          e.preventDefault()
          if (checkIfDisabled()) {
            return alert('No avatar selected or it was not changed')
          }
          onAvatarChange({ file: avatarFile })
        }}>
        <FormTitle>Avatar</FormTitle>
        <FileInput
          onChange={file => {
            setUpdated(true)
            setAvatarFile(file)
          }}
          fileTypes={["image/png", "image/jpeg"]}
          fileSize={5000}
          className={styles.fileInput}
          file={avatarFile}
        />
        <Button
          modifier='style_dark'
          type='submit'
          className={styles.button}
        >
          Update avatar
        </Button>
      </Form>
    </Container>
  </Main>
}

export default UpdateAvatar
