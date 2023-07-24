
resource "aws_alb" "this" {
  # checkov:skip=CKV_AWS_150:Don't enable deletion protection
  name                       = "${local.team}-${local.project}-${terraform.workspace}-alb"
  internal                   = false
  drop_invalid_header_fields = true
  load_balancer_type         = "application"
  subnets                    = data.terraform_remote_state.vpc.outputs.public_subnets
  security_groups            = concat([aws_security_group.load_balancer_security_group.id], var.alb_additional_security_groups)

  # TODO: Create log bucket
  #   access_logs {
  #     bucket  = data.terraform_remote_state.platform.outputs.log_bucket
  #     prefix  = "alb/${var.name}"
  #     enabled = true
  #   }
}

resource "aws_security_group" "load_balancer_security_group" {
  vpc_id      = data.terraform_remote_state.vpc.outputs.vpc_id
  description = "${local.team} ${local.project} alb security group"
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_security_group_rule" "alb_allow_http" {
  # checkov:skip=CKV_AWS_260:Allow for all ingress to port 80
  type              = "ingress"
  description       = "Allow Whitelisted HTTP Traffic access to the load balancer"
  from_port         = 80
  to_port           = 80
  protocol          = "TCP"
  cidr_blocks       = var.ip_securelist
  security_group_id = aws_security_group.load_balancer_security_group.id
}

resource "aws_security_group_rule" "alb_allow_https" {
  type              = "ingress"
  description       = "Allow Whitelisted HTTPS Traffic access to the load balancer "
  from_port         = 443
  to_port           = 443
  protocol          = "TCP"
  cidr_blocks       = var.ip_securelist
  security_group_id = aws_security_group.load_balancer_security_group.id
}

resource "aws_security_group_rule" "allow_egress" {
  type              = "egress"
  description       = "Allow the load balancer to egress anywhere"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.load_balancer_security_group.id
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_alb.this.id
  port              = "80"
  protocol          = "HTTP"
#   TODO: Re-enable when we have https
  #   default_action {
  #     type = "redirect"

  #     redirect {
  #       port        = "443"
  #       protocol    = "HTTPS"
  #       status_code = "HTTP_301"
  #     }
  #   }
}
