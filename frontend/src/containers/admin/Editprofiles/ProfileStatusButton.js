import React, {Component} from 'react'
import { Link } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { adminStyles } from 'styles';


class ProfileStatusButton extends Component {

  render() {
    const { link, title, requireApproval, profileId, classes } = this.props;
    let buttonClasses = [classes.button, classes.adminTalentStatusButton];

    if (requireApproval) buttonClasses.push(classes.adminTalentStatusApproved);

    return (
        <Link
            to={{
                pathname: link,
                state: { profileId: profileId }
            }}
        >
            <Button variant="contained" size="large" fullWidth className={buttonClasses}>
            <Typography className={[classes.bold, classes.adminTalentStatusButtonText]}>
                { title }
            </Typography>
            </Button>
        </Link>
    );
  }
}

export default withStyles(adminStyles)(ProfileStatusButton);